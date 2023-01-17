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

- **/help**: This command allows users to view a list of available commands and their descriptions.

- **/gameserver_start**: This command allows users with administrator permissions to start a Nitrado game server. It requires the Nitrado server ID and a bearer token for authentication.

- **/gameserver_stop**: This command allows users with administrator permissions to stop a Nitrado game server. It requires the Nitrado server ID and a bearer token for authentication.

- **/gameserver_restart**: This command allows users with administrator permissions to restart a Nitrado game server. It requires the Nitrado server ID and a bearer token for authentication.

- **/gameserver_status**: This command allows users to check the status of a Nitrado game server. It requires the Nitrado server ID and a bearer token for authentication.

- **/gameserver_info**: This command allows users to retrieve information about a Nitrado game server such as the server name, ID, and current players. It requires the Nitrado server ID and a bearer token for authentication.

- **/list_gameservers**: This command allows users to view a list of all Nitrado game servers on the server.

- **/add_gameserver**: This command allows users with administrator permissions to add a Nitrado game server to the server list. It requires the Nitrado server ID, a bearer token for authentication, and a name for the server.

- **/remove_gameserver**: This command allows users with administrator permissions to remove a Nitrado game server from the server list. It requires the Nitrado server ID and a bearer token for authentication.

It's important to note that some commands such as /gameserver_start, /gameserver_stop, /gameserver_restart, /add_gameserver and /remove_gameserver require administrator permissions.

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
