# Dodocord

Welcome to Dodocord, a bot designed to manage Ark game servers hosted by Nitrado. It allows you to easily control your game servers and retrieve information about them directly from your discord server.

Dodocord is a multi-server bot, which means it can be used on multiple discord servers simultaneously.

This project is open source, which means that the code is available for anyone to use, modify, and contribute to. For users who only want to use the bot, it can be invited to your server by clicking the invite button.

If you're interested in contributing to the development of Dodocord, please read the CONTRIBUTING.md for information on how to do so.

**IMPORTANT:** If you are only here to use the bot, you don't need to read the setup part, you only have to invite the bot to your server by clicking the invite button.
The setup part is only for people who want to run the bot on their own environment and contribute to the project.
You can find the list of available commands and how to use them in the readme file.
Thank you for using Dodocord.

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

## How to obtain all the keys and tokens required

To get the **bot token**, you will need to create a bot on the Discord Developer Portal. Once you have created the bot, you will be given a token that you can use to authenticate the bot with the Discord API.

To get the **AWS Key** and **AWS Secret**, you will need to create an IAM user with the appropriate permissions to access the KMS services on the AWS Management Console. Once you have created the user, you will be given an access key and secret key that you can use to access the KMS services.

To get the **KMS Key**, you will need to create a key on the AWS Management Console. Once you have created the key, you will be given a key ID that you can use to encrypt and decrypt data.

It's important to not share or make public these tokens and keys, they should be kept private and only be used on your server or machine.

## How to add a Nitrado Game Server using the **/add_gameserver** command

To get the bearer token needed to use the **/add_gameserver** command, you will need to first create an account on the Nitrado website. Once you have created an account, you will need to log in and navigate to the "API" section. There, you will be able to create a new API token which will be used as the bearer token.

You can also manage your API tokens and view their expiration dates. It's important to note that you should keep your bearer token private and not share it with anyone else.

To find the Nitrado server ID, you will need to navigate to the game servers section in the Nitrado website and select the game server you want to add. The server ID can be found in the URL of the server page.

You will need to have the Nitrado server ID and the bearer token to use the **/add_gameserver** command. Once you have those, you can use the command in the discord server to add the server to the list and retrieve the server's information.

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
