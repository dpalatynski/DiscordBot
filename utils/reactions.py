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
        embed = Embed(color=0x2ca5f1)
        embed.set_image(url=gif)
        await ctx.send(embed=embed)

    @commands.command(name='anger',
                      hidden=True,
                      aliases=['angry', 'wrrr', 'wrr'])
    async def anger(self, ctx):
        gif = 'https://c.tenor.com/Q3406JOSa5wAAAAC/angry-anger.gif'
        embed = Embed(color=0x2ca5f1)
        embed.set_image(url=gif)
        await ctx.send(embed=embed)

    @commands.command(name='loveyou',
                      hidden=True,
                      aliases=['iloveu', 'loveu', 'iloveyou', 'luvu'])
    async def loveyou(self, ctx):
        gif = 'https://c.tenor.com/1hyzQj_f5PgAAAAC/kitten-love.gif'
        embed = Embed(color=0x2ca5f1)
        embed.set_image(url=gif)
        await ctx.send(embed=embed)

    @commands.command(name='what',
                      hidden=True,
                      aliases=['wut', 'whaat'])
    async def what(self, ctx):
        gif = 'https://c.tenor.com/wamL_NeO8-wAAAAd/bunnies-what.gif'
        embed = Embed(color=0x2ca5f1)
        embed.set_image(url=gif)
        await ctx.send(embed=embed)

    @commands.command(name='fuckoff',
                      hidden=True,
                      aliases=['fuckyou'])
    async def fuckoff(self, ctx):
        gif = 'https://c.tenor.com/HWBMmc8g6p4AAAAC/fuck-fuck-you.gif'
        embed = Embed(color=0x2ca5f1)
        embed.set_image(url=gif)
        await ctx.send(embed=embed)

    @commands.command(name='triggered',
                      hidden=True,
                      aliases=['trigger'])
    async def triggered(self, ctx):
        gif = 'https://c.tenor.com/x4f7WA4aUcQAAAAC/hamster-triggered.gif'
        embed = Embed(color=0x2ca5f1)
        embed.set_image(url=gif)
        await ctx.send(embed=embed)

    @commands.command(name='sad',
                      hidden=True,
                      aliases=['sorrow', 'sadness', 'painful'])
    async def sad(self, ctx):
        gif = 'https://c.tenor.com/fr-REzQ29BQAAAAC/sad-eyes-so-sad.gif'
        embed = Embed(color=0x2ca5f1)
        embed.set_image(url=gif)
        await ctx.send(embed=embed)

    @commands.command(name='happy',
                      hidden=True,
                      aliases=['happiness', 'glad', 'good', 'enjoy'])
    async def happy(self, ctx):
        gif = 'https://c.tenor.com/wWVQDp6Q9hYAAAAC/shaq-shaquille-o-neal.gif'
        embed = Embed(color=0x2ca5f1)
        embed.set_image(url=gif)
        await ctx.send(embed=embed)

    @commands.command(name='popcorn',
                      hidden=True)
    async def popcorn(self, ctx):
        gif = 'https://c.tenor.com/X0uJSBblnXAAAAAC/stephen-colbert-popcorn.gif'
        embed = Embed(color=0x2ca5f1)
        embed.set_image(url=gif)
        await ctx.send(embed=embed)

    @commands.command(name='pathetic',
                      hidden=True)
    async def pathetic(self, ctx):
        gif = 'https://c.tenor.com/D3w8y09N4MsAAAAC/gordon-ramsay-master-chef.gif'
        embed = Embed(color=0x2ca5f1)
        embed.set_image(url=gif)
        await ctx.send(embed=embed)

    @commands.command(name='aww',
                      hidden=True,
                      aliases=['sweet', 'awww', 'sweetie'])
    async def aww(self, ctx):
        gif = 'https://c.tenor.com/Td_dBCzwFRQAAAAC/aww-cute.gif'
        embed = Embed(color=0x2ca5f1)
        embed.set_image(url=gif)
        await ctx.send(embed=embed)

    @commands.command(name='cmon',
                      hidden=True)
    async def cmon(self, ctx):
        gif = 'https://c.tenor.com/fLcQ7O0kJgEAAAAC/cmonbro-cmon.gif'
        embed = Embed(color=0x2ca5f1)
        embed.set_image(url=gif)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Reactions(client))
