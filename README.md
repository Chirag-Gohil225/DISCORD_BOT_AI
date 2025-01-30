## DISCORD BOT FOR AI USING OLLAMA
## Discord Bot

This is a Discord bot built using Python and the `discord.py` library. The bot can respond to user messages and provide status updates.

## Features

- Responds to user messages with a custom response.
- Provides a status update command.
### Step 1) Set up and download the Ollama and LLM of your choice. 
https://ollama.com/ also to get a restrictions free experience.. you can run abliterated models.

``` $ ollama run <your model> ```
-- after setting up Ollama

### Step 1) Create the bot in discord developer portal, customize it, get TOKEN AND CLIENT ID and set the permissions up.
https://discord.com/developers/applications

--> TURN ON 'Server Members Intent' and 'Message Content Intent' in Privileged Gateway Intents, found in #bot in Discord Dev. Portal

--> you can add the bot in your server in #INSTALLATION in the discord dev portal or alternatively you can use this link, 

```https://discord.com/api/oauth2/authorize?&client_id=<CLIENTID>cope=bot&permissions=8```, relpace <CLIENTID> with actual CLIENTID.

### Step 2) Setup

1. Clone the repository.
2. Create a virtual environment and activate it:
    ```sh
    python -m venv bot_env ## bot_env can me named anything
    source bot_env/bin/activate  # On Windows use `bot_env\Scripts\activate`, as this was done on a mac
    ```
3. Install the required dependencies:
    ```sh
    pip install python-dotenv discord.py
    ```
4. Create a `.env` file in the root directory and add your Discord bot token and client ID:
    ```env
    DISCORD_BOT_TOKEN='your_discord_bot_token'
    CLIENT_ID=your_client_id
    ```
5. Run the bot:
    ```sh
    python3 app.py
    ```

## Commands

- `/l <text>`: The bot will respond to the provided text.
- `/sts`: The bot will provide a status update.

## Dependencies

- [discord.py](https://discordpy.readthedocs.io/en/stable/)
- [ollama](https://ollama.com/)
- `python-dotenv`

## License

This project is licensed under the MIT License.

UPDATED ON 31th JAN 2025
