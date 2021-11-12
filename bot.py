from discord.ext.commands import Bot
import discord
import os
from flask import Flask
from threading import Thread


TOKEN = os.environ['BOT_TOKEN_DRACKS']
os.environ['MPLCONFIGDIR'] = os.getcwd() + "/configs/"
BOT_PREFIX = '.'

intents = discord.Intents.all()
client = Bot(command_prefix=BOT_PREFIX, intents=intents)

app = Flask("")


@app.route('/')
def home():
    return "Bot is online!"


def run():
    app.run(host='0.0.0.0',port=8080)


def keep_alive():
    t = Thread(target=run)
    t.start()


@client.event
async def on_ready():
    client.load_extension("utils.messages")
    client.load_extension("utils.members")
    client.load_extension("utils.top")
    client.load_extension("utils.fun")
    client.load_extension("utils.stats")
    client.load_extension("utils.admin")
    client.load_extension("utils.reactions")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=".help"))


@client.command(hidden=True)
async def load(ctx, extension):
    client.load_extension(f'utils.{extension}')


keep_alive()
client.run(TOKEN)

