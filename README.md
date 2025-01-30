# Discord Bot for AI using Ollama

This is a Discord bot built using Python and the `discord.py` library. The bot can respond to user messages and provide status updates.

## Features

- Responds to user messages with a custom response.
- Provides a status update command.
- Use locally hosted LLM in discord bot.

## Setup

### Step 1: Set up and download Ollama and the LLM of your choice

- Visit [Ollama](https://ollama.com/) to set up and download the LLM. For a restrictions-free experience, you can run [abliterated models](https://ollama.com/search?q=abliterated)

```sh
ollama run <your model>
```

### Step 2: Create the bot in the Discord Developer Portal

- Visit [Discord Developer Portal](https://discord.com/developers/applications) to create your bot, customize it, and get the TOKEN and CLIENT_ID.
- Turn on "Server Members Intent" and "Message Content Intent" found under "Privileged Gateway Intents" in BOT section on the sidebar
- Add the bot to your server by going to INSTALLATION in the sidebar or alternatively, ```https://discord.com/api/oauth2/authorize?&client_id=<CLIENTID>&scope=bot&permissions=8``` using this link and replacing ```<CLIENT_ID>``` with your actual id.

### Step 3: Set up the project

- Clone the repository
- Create a virtual envirnoment and activate it
  ```sh
  python3 -m venv bot_env ##you can name "bot_env" anything
  source bot_env/bin/activate #for_mac
  ```
- Install the required dependencies:
  ```sh
  pip install python-dotenv discord.py
  ```
- Create a ```.env``` in the project directory and add your Discord bot token and Client id there
  ```DISCORD_BOT_TOKEN='your_discord_bot_token'```

  ```CLIENT_ID=your_client_id```
- Before running the bot, update ```<YOUR MODEL NAME>``` to your actual model name, which can be found using
  ```sh
  ollama list
  ```
  and copying the name the model of your choice and pasting it in the code.
- Run the bot
  ```sh
  python3 app.py
  ```

## Commands

- ```/l <text>``` The bot will respond to the provided text
- ```/sts``` to check if the bot is online or not, WILL REPLY NOTHING WHEN OFFLINE
- Use ```"/"``` as a prefix; pinging the bot doesnt work...yet.

## Dependencies

- [Discord.py](https://discordpy.readthedocs.io/en/stable/)
- [Ollama](https://ollama.com/)
- ```python-dotenv```

## License

This project is licensed under the GPL-3.0 license

``` LAST UPDATED ON 31th JAN 2025```
