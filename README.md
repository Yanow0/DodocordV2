# Dodocord

Dodocord is a bot designed to manage Ark game servers hosted by Nitrado. It allows you to easily control your game servers and retrieve information about them directly from your discord server.

## Setting up your own token

In order to use your own token, you need to set up an environment variable named TOKEN with your bot token.
## Available commands

    /help: Get a list of available commands.
    /gameserver_start: Start a Nitrado game server.
    /gameserver_stop: Stop a Nitrado game server.
    /gameserver_restart: Restart a Nitrado game server.
    /gameserver_status: Get the status of a Nitrado game server.
    /gameserver_info: Get information of a Nitrado game server.
    /list_gameservers: List all Nitrado game servers on the server.
    /add_gameserver: Add a Nitrado game server to the server list.
    /remove_gameserver: Remove a Nitrado game server from the server list.

Note: Some commands require administrator permissions.
## Running the bot

- Make sure you have Python3 installed on your machine.
- Install the required dependencies by running the following command:

```bash
pip install -r requirements.txt
```

- Run the bot by executing the following command:

```bash
python run.py
```

## Contributing

If you would like to contribute to the development of Dodocord, please read the CONTRIBUTING.md for information on how to do so.
