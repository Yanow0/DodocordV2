from cryptography.fernet import Fernet

import constants
import requests
import discord
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord.ext import commands
from discord import app_commands
from typing import List
from ..db import db
from dotenv import load_dotenv
import os
import boto3

kms = boto3.client('kms')

load_dotenv()
TOKEN = os.getenv('TOKEN')

intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix=constants.PREFIX, intents=intents)

db.init()
scheduler = AsyncIOScheduler()
db.autosave(scheduler)


def run():
    client.run(TOKEN)


@client.event
async def on_guild_join(guild):
    embed = discord.Embed(title="Dodocord",
                          description="I am a bot designed to manage Ark game servers hosted by Nitrado",
                          color=0x00ff00)
    embed.add_field(name="Commands",
                    value="Use /help to get a list of available commands")
    embed.set_thumbnail(url="attachment://assets/img/dodocord.jpg")
    embed.set_footer(text="Powered by Dodocord")
    try:
        joinchannel = guild.system_channel
        await joinchannel.send(embed=embed, file=discord.File('assets/img/dodocord.jpg'))
    except discord.Forbidden:
        joinchannel = guild.text_channels[0]
        await joinchannel.send(embed=embed, file=discord.File('assets/img/dodocord.jpg'))

    if not db.record("SELECT server_id FROM servers WHERE server_id = ?", guild.id):
        db.execute("INSERT INTO servers (server_id, server_name, owner_id, main_channel_id) VALUES (?,?,?,?)",
                   guild.id, guild.name, guild.owner.id, joinchannel.id)
        db.commit()


async def add_gameserver(interaction: discord.Interaction, nitrado_server_id: int, bearer_token: str,
                         nitrado_server_name: str):
    # check if the server already exists in the list
    existing_server = db.record("SELECT nitrado_server_id FROM nitrado_servers WHERE nitrado_server_id = ?",
                                nitrado_server_id)
    if not existing_server:
        key = Fernet.generate_key()  # generate a new key
        # encrypt the key using KMS
        encrypted_key = kms.encrypt(KeyId='alias/my-kms-key', Plaintext=key)['CiphertextBlob']
        cipher = Fernet(key)
        ciphertext = cipher.encrypt(bearer_token.encode())
        # store the encrypted key and ciphertext in the database
        db.execute(
            "INSERT INTO nitrado_servers (server_id, encrypted_key, ciphertext, nitrado_server_id, "
            "nitrado_server_name) VALUES (?,?,?,?,?)",
            interaction.guild.id, encrypted_key, ciphertext, nitrado_server_id, nitrado_server_name)
        db.commit()
        embed = discord.Embed(title="Server added to the list", color=discord.Color.green())
        await interaction.response.send_message(embed=embed, ephemeral=True)
    else:
        embed = discord.Embed(title="Server already exists in the list", color=discord.Color.red())
        await interaction.response.send_message(embed=embed, ephemeral=True)


@client.tree.command(name="list_gameservers", description="List all Nitrado game servers on the server.")
async def list_gameservers(interaction: discord.Interaction):
    nitrado_servers = db.records(
        "SELECT nitrado_server_id, nitrado_server_name FROM nitrado_servers WHERE server_id = ?",
        interaction.guild.id)
    if nitrado_servers:
        server_list = "\n".join([f"{server[0]}: {server[1]}" for server in nitrado_servers])
        embed = discord.Embed(title="Nitrado Game Servers", description=server_list, color=discord.Color.green())
        await interaction.response.send_message(embed=embed, ephemeral=True)
    else:
        embed = discord.Embed(title="No Nitrado game servers found on this server.", color=discord.Color.red())
        await interaction.response.send_message(embed=embed, ephemeral=True)


async def server_autocompletion(
        interaction: discord.Interaction,
        current: str
) -> List[app_commands.Choice[int]]:
    nitrado_servers = db.records(
        "SELECT nitrado_server_id, nitrado_server_name FROM nitrado_servers WHERE server_id = ?",
        interaction.guild.id)
    choices = []
    for server in nitrado_servers:
        if current.lower() in server[1].lower():
            choices.append(app_commands.Choice(name=server[1], value=server[1]))
    return choices


@client.tree.command(name="gameserver_status", description="Get the status of a Nitrado game server.")
@app_commands.autocomplete(item=server_autocompletion)
async def gameserver_status(interaction: discord.Interaction, item: str):
    server_info = nitrado_server_id, nitrado_server_name, headers = await get_server_info(interaction, item)
    if server_info is None:
        return
    response = requests.get('https://api.nitrado.net/services/' + str(nitrado_server_id) + '/gameservers',
                            headers=headers)
    if response.status_code == 200:
        json = response.json()
        data = json['data']
        server_status = data['gameserver']['status']
        if server_status == 'stopped':
            embed = discord.Embed(title="Server Status", description="The server is currently stopped",
                                  color=0xff0000)
        else:
            if "server_name" in data['gameserver']['query']:
                server_name = data['gameserver']['query']['server_name']
                server_map = data['gameserver']['query']['map']
                server_players = data['gameserver']['query']['player_current']
                embed = discord.Embed(title="Server Status", color=0x00ff00)
                embed.add_field(name="Server name", value=server_name, inline=True)
                embed.add_field(name="Server status", value=server_status.capitalize(), inline=True)
                embed.add_field(name="Map name", value=server_map, inline=True)
                embed.add_field(name="Number of players online", value=server_players, inline=True)
            else:
                embed = discord.Embed(title="Server Status",
                                      description="The server is not stopped, but is not accessible right now. It "
                                                  "is probably starting up.",
                                      color=0x00ff00)
        await interaction.response.send_message(embed=embed, ephemeral=True)
    else:
        message = f"Error: {response.status_code}"
        await interaction.response.send_message(message, ephemeral=True)


@commands.has_permissions(administrator=True)
@client.tree.command(name="gameserver_stop", description="Stop a Nitrado game server.")
@app_commands.autocomplete(item=server_autocompletion)
async def gameserver_stop(interaction: discord.Interaction, item: str):
    server_info = nitrado_server_id, nitrado_server_name, headers = await get_server_info(interaction, item)
    if server_info is None:
        return

    params = {
        'message': 'Stopping server from discord bot',
        'stop_message': 'Someone stopped the server using the Discord Bot'
    }
    response = requests.post('https://api.nitrado.net/services/' + str(nitrado_server_id) + '/gameservers/stop',
                             headers=headers,
                             params=params)
    if response.status_code == 200:
        message = discord.Embed(title=f"Server {nitrado_server_name}", description="is stopping...",
                                color=discord.Color.green())
        await interaction.response.send_message(embed=message)
    else:
        data = response.json()
        message_status = f"Error: {response.status_code}"
        message_info = data['message']
        error_message = discord.Embed(title=message_status, description=message_info, color=discord.Color.red())
        await interaction.response.send_message(embed=error_message)


@commands.has_permissions(administrator=True)
@client.tree.command(name="gameserver_restart", description="Restart a Nitrado game server.")
@app_commands.autocomplete(item=server_autocompletion)
async def gameserver_restart(interaction: discord.Interaction, item: str):
    server_info = nitrado_server_id, nitrado_server_name, headers = await get_server_info(interaction, item)
    if server_info is None:
        return
    params = {
        'message': 'Restarting server from discord bot',
        'restart_message': 'Someone restarted the server using the Discord Bot'
    }
    response = requests.post('https://api.nitrado.net/services/' + str(nitrado_server_id) + '/gameservers/restart',
                             headers=headers,
                             params=params)
    if response.status_code == 200:
        embed = discord.Embed(title="Server Restart", description=f"Server {nitrado_server_name} is restarting...",
                              color=discord.Color.green())
        await interaction.response.send_message(embed=embed)
    else:
        data = response.json()
        message_status = f"Error: {response.status_code}"
        message_info = data['message']
        embed = discord.Embed(title="Server Restart", description=f"{message_status}\n{message_info}",
                              color=discord.Color.red())
        await interaction.response.send_message(embed=embed)


@client.tree.command(name="players_online", description="Players currently online on a Nitrado game server.")
@app_commands.autocomplete(item=server_autocompletion)
async def players_online(interaction: discord.Interaction, item: str):
    embed = discord.Embed(title="Online players", description="Loading...", color=discord.Color.green())
    await interaction.response.send_message(embed=embed)
    server_info = nitrado_server_id, nitrado_server_name, headers = await get_server_info(interaction, item)
    if server_info is None:
        return
    response = requests.get('https://api.nitrado.net/services/' + str(nitrado_server_id) + '/gameservers/games/players',
                            headers=headers)
    if response.status_code == 200:
        data = response.json()['data']
        online_players = []
        for player in data['players']:
            if player['online']:
                online_players.append(player['name'])

        if len(online_players) == 0:
            embed = discord.Embed(title="Online players", description=f"No players online on {nitrado_server_name}.")
            await interaction.edit_original_response(embed=embed)
        else:
            embed = discord.Embed(title="Online players", description=f"Players online on {nitrado_server_name}:")
            embed.add_field(name="Players", value="\n".join(online_players), inline=False)

        await interaction.edit_original_response(embed=embed)
    else:
        embed = discord.Embed(title="Online players",
                              description=f"Cannot access current online players on {nitrado_server_name}, the server "
                                          f"is probably stopped.",
                              color=0xff0000)
        await interaction.edit_original_response(embed=embed)


async def get_server_info(interaction: discord.Interaction, input_server_name: str):
    nitrado_servers = db.records(
        "SELECT nitrado_server_id, nitrado_server_name FROM nitrado_servers WHERE server_id = ?", interaction.guild.id)
    nitrado_server_id = None
    nitrado_server_name = None
    for server in nitrado_servers:
        if input_server_name.lower() == server[1].lower():
            nitrado_server_id = server[0]
            nitrado_server_name = server[1]
            break
    if nitrado_server_id is None:
        embed = discord.Embed(title="Server not found",
                              description="No server found with this name. Please check the name and try again.",
                              color=0xff0000)
        await interaction.response.edit_message(embed=embed, ephemeral=True)
        return

    # retrieve the encrypted key and ciphertext from the database
    encrypted_key = db.field("SELECT encrypted_key FROM nitrado_servers WHERE nitrado_server_id = ?", nitrado_server_id)
    ciphertext = db.field("SELECT ciphertext FROM nitrado_servers WHERE nitrado_server_id = ?", nitrado_server_id)
    # decrypt the key using KMS
    key = kms.decrypt(CiphertextBlob=encrypted_key)['Plaintext']
    cipher = Fernet(key)
    bearer_token = cipher.decrypt(ciphertext).decode()
    headers = {
        'Authorization': 'Bearer ' + bearer_token,
    }
    return nitrado_server_id, nitrado_server_name, headers


@client.event
async def on_ready():
    print('Bot is ready.')
    scheduler.start()
    try:
        synced = await client.tree.sync()
        print(f"Synced {len(synced)} commands.")
    except Exception as e:
        print(e)
