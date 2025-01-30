import os
import discord
from discord.ext import commands
from ollama import chat as ollama_chat
from ollama import ChatResponse
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True 

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f"Bot is ready as {bot.user.name}")

@bot.command(name="l")
async def ask(ctx, *, message=None):
    if not message:
        await ctx.send("```/l <text>``` TEXT NOT FOUND AFTER /l")
        return

    response: ChatResponse = ollama_chat(model='<YOUR MODEL HERE>', messages=[. ##DONT FORGET TO REPLACE YOUR MODEL NAME HERE
        {
            'role': 'assistant',
            'content': 'You are an assistant who answers to the questions concisely in 1000characters',
        },
        {
            'role': 'user',
            'content': message,
        },
    ])
    await ctx.send(response.message.content)

@bot.command(name="sts")
async def status(ctx):
    await ctx.send("ONLINE")


bot.run(os.getenv("DISCORD_BOT_TOKEN"))

