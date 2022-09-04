from discord.ext import commands
import discord
import os
from flask import Flask
from threading import Thread
import asyncio


TOKEN = os.environ['BOT_TOKEN_DRACKS']
os.environ['MPLCONFIGDIR'] = os.getcwd() + "/configs/"
BOT_PREFIX = '.'

intents = discord.Intents.all()
intents.message_content = True

client = commands.Bot(command_prefix=BOT_PREFIX,
                      intents=intents,
                      activity=discord.Activity(
                                                type=discord.ActivityType.listening,
                                                name=".help"))

app = Flask("")


@app.route('/')
def home():
    return "Bot is online!"


def run():
    app.run(host='0.0.0.0', port=8080)


def keep_alive():
    t = Thread(target=run)
    t.start()


@client.event
async def on_ready():
    await client.load_extension("utils.messages")
    await client.load_extension("utils.members")
    await client.load_extension("utils.top")
    await client.load_extension("utils.fun")
    await client.load_extension("utils.stats")
    await client.load_extension("utils.admin")
    await client.load_extension("utils.reactions")
    await client.load_extension("utils.facebook")
    await client.load_extension("utils.server_tools")


async def main():
    await on_ready()
    await client.start(TOKEN)


keep_alive()
asyncio.run(main())
