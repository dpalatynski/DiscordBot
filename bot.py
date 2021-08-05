from discord.ext.commands import Bot
import discord


TOKEN = 'token'
BOT_PREFIX = '.'

intents = discord.Intents.all()
client = Bot(command_prefix=BOT_PREFIX, intents=intents)


@client.event
async def on_ready():
    print('Bot is online!')
    client.load_extension("utils.messages")
    client.load_extension("utils.members")
    client.load_extension("utils.top")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Python"))


@client.command(hidden=True)
async def load(ctx, extension):
    client.load_extension(f'utils.{extension}')


client.run(TOKEN)
