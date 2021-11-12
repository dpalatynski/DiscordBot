from discord.ext import commands
from discord import Embed


class Reactions(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name='muah',
                      hidden=True,
                      aliases=['mua', 'kisses', 'kiss'])
    async def muah(self, ctx):
        gif = 'https://c.tenor.com/7t_cEhNQxWIAAAAC/muah-minions.gif'
        embed = Embed(title='Muah!', color=0x2ca5f1)
        embed.set_image(url=gif)
        await ctx.send(embed=embed)

    @commands.command(name='anger',
                      hidden=True,
                      aliases=['angry', 'wrrr', 'wrr'])
    async def anger(self, ctx):
        gif = 'https://c.tenor.com/Q3406JOSa5wAAAAC/angry-anger.gif'
        embed = Embed(title='Wrrr!', color=0x2ca5f1)
        embed.set_image(url=gif)
        await ctx.send(embed=embed)

    @commands.command(name='loveyou',
                      hidden=True,
                      aliases=['iloveu', 'loveu', 'iloveyou', 'luvu'])
    async def loveyou(self, ctx):
        gif = 'https://c.tenor.com/1hyzQj_f5PgAAAAC/kitten-love.gif'
        embed = Embed(title='Love you!', color=0x2ca5f1)
        embed.set_image(url=gif)
        await ctx.send(embed=embed)

    @commands.command(name='what',
                      hidden=True,
                      aliases=['wut', 'whaat'])
    async def what(self, ctx):
        gif = 'https://c.tenor.com/wamL_NeO8-wAAAAd/bunnies-what.gif'
        embed = Embed(title='Whaaat?', color=0x2ca5f1)
        embed.set_image(url=gif)
        await ctx.send(embed=embed)

    @commands.command(name='fuckoff',
                      hidden=True,
                      aliases=['fuckyou'])
    async def fuckoff(self, ctx):
        gif = 'https://c.tenor.com/HWBMmc8g6p4AAAAC/fuck-fuck-you.gif'
        embed = Embed(title='Fuck off!', color=0x2ca5f1)
        embed.set_image(url=gif)
        await ctx.send(embed=embed)

    @commands.command(name='triggered',
                      hidden=True,
                      aliases=['trigger'])
    async def triggered(self, ctx):
        gif = 'https://c.tenor.com/x4f7WA4aUcQAAAAC/hamster-triggered.gif'
        embed = Embed(title='Triggered', color=0x2ca5f1)
        embed.set_image(url=gif)
        await ctx.send(embed=embed)

    @commands.command(name='sad',
                      hidden=True,
                      aliases=['sorrow', 'sadness', 'painful'])
    async def sad(self, ctx):
        gif = 'https://c.tenor.com/fr-REzQ29BQAAAAC/sad-eyes-so-sad.gif'
        embed = Embed(title='Sad', color=0x2ca5f1)
        embed.set_image(url=gif)
        await ctx.send(embed=embed)

    @commands.command(name='happy',
                      hidden=True,
                      aliases=['happiness', 'glad', 'good', 'enjoy'])
    async def happy(self, ctx):
        gif = 'https://c.tenor.com/wWVQDp6Q9hYAAAAC/shaq-shaquille-o-neal.gif'
        embed = Embed(title='Enjoy!', color=0x2ca5f1)
        embed.set_image(url=gif)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Reactions(client))
