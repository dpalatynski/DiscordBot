from discord.ext import commands
from discord import Embed
from facebook_scraper import get_posts


class Facebook(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name='facebook',
                      brief='Retrieves the latest posts from Facebook public profiles',
                      description='-> ".facebook [user] [number]" - sends a specific amount of the latest messages \n'
                                  '\n'
                                  'You can\'t retrieve more than 10 messages in one query')
    async def facebook(self, ctx, user, number):
        try:
            number = int(number)
        except ValueError and TypeError:
            number = 1
        if number > 10:
            embed = Embed(color=0xff0000)
            embed.add_field(name='Warning', value=':no_entry: You can\'t retrieve more than 10 last messages.')
            await ctx.send(embed=embed)
        else:
            counter = 0
            for post in get_posts(user, pages=3, cookies='cookies.json'):
                embed = Embed(color=0x2ca5f1)
                if post['image'] is not None:
                    embed.set_image(url=post['image'])
                embed.add_field(name=post['time'], value=post['text'])
                embed.set_footer(text=post['post_id'])

                await ctx.send(embed=embed)

                counter += 1
                if counter >= number:
                    break

    async def cog_command_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            embed = Embed(color=0xff0000)
            embed.add_field(name='Error', value=':no_entry: I can\'t retrieve any information. Please try again later.')

            await ctx.send(embed=embed)


async def setup(client):
    await client.add_cog(Facebook(client))
