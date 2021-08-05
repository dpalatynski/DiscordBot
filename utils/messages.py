from discord.ext import commands


class Messages(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name='messages',
                      brief='How much messages were sent in this channel?',
                      description='Function returns a total number of messages, which were sent already in this '
                                  'channel. Use !messages [user] to return a number of messages sent by [user].',
                      aliases=['msgs'])
    async def messages(self, ctx, user=None):
        counter = 0
        if user:
            async for message in ctx.channel.history(limit=None):
                if str(message.author.id) == str(user)[3:-1]:
                    counter += 1
            if counter == 1:
                reply = "User {} sent {} message in the channel {}.".format(user, counter, ctx.channel.mention)
            else:
                reply = "User {} sent {} messages in the channel {}.".format(user, counter, ctx.channel.mention)
            await ctx.send(reply)
        else:
            async for _ in ctx.channel.history(limit=None):
                counter += 1
            if counter == 1:
                reply = "There was {} message in the channel {}.".format(counter, ctx.channel.mention)
            else:
                reply = "There were {} messages in the channel {}.".format(counter, ctx.channel.mention)
            await ctx.send(reply)


def setup(client):
    client.add_cog(Messages(client))
