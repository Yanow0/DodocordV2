# Dodocord

Dodocord is a bot designed to manage Ark game servers hosted by Nitrado. It allows you to easily control your game servers and retrieve information about them directly from your discord server.

## Environment variables

In order to run the Dodocord bot, you will need to set up the following environment variables:

    TOKEN: This variable stores the bot token that is used to authenticate the bot with the Discord API.
    AWS_KEY: This variable stores the AWS Key used to access the KMS services.
    AWS_SECRET: This variable stores the AWS Secret used to access the KMS services.
    KMS_KEY: This variable stores the key used to encrypt and decrypt the bearer token that is used to authenticate requests to the Nitrado API.

You can set these environment variables by creating a .env file in the root directory of the project and adding the following lines to it:

    TOKEN=your_bot_token
    AWS_KEY=your_aws_key
    AWS_SECRET=your_aws_secret
    KMS_KEY=your_kms_key

You should replace your_bot_token, your_aws_key, your_aws_secret, and your_kms_key with the actual values for your bot token, AWS Key, AWS Secret, and KMS key

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
