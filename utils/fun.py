from discord.ext import commands
import requests
import asyncio
import random


class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name='joke',
                      brief='Let\'s tell a joke!',
                      description='-> ".joke" - generates a random joke')
    async def joke(self, ctx):
        url = 'https://official-joke-api.appspot.com/random_joke'
        joke = requests.get(url).json()

        await ctx.send(joke["setup"])
        await asyncio.sleep(2)
        await ctx.send(joke['punchline'])

    @commands.command(name='fact',
                      brief='Do you know that ...?',
                      description='-> ".fact" - generates a random fact')
    async def fact(self, ctx):
        url = 'https://uselessfacts.jsph.pl/random.json?language=en'
        fact = requests.get(url).json()

        await ctx.send(fact['text'])

    @commands.command(name='roll',
                      brief='Roll a dice',
                      description='-> ".roll" - rolls a dice \n'
                                  '-> ".roll [number]" - rolls a number of dices')
    async def roll(self, ctx, number_of_dice=None):
        try:
            number_of_dice = int(number_of_dice)
        except ValueError and TypeError:
            number_of_dice = 1

        results = '%s You rolled: ' % ctx.message.author.mention
        for i in range(number_of_dice):
            results += str(random.randint(1, 6)) + ', '

        await ctx.send(results[:-2])

    @commands.command(name='randint',
                      brief='Get a random integer',
                      description='-> ".randint" - generates randomly 0 or 1 \n'
                                  '-> ".randint [min] [max]" - generates a random number in a given interval')
    async def randint(self, ctx, bottom=0, top=1):
        if top < bottom:
            result = 'The second number should be higher or equal than the first one.'
        else:
            bottom, top = int(bottom), int(top)
            result = str(random.randint(bottom, top))

        await ctx.send(result)


def setup(client):
    client.add_cog(Fun(client))
