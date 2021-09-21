from discord.ext import commands


class Messages(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name='messages',
                      brief='How many messages were sent?',
                      description='-> ".messages" - returns a number of messages in this channel \n'
                                  '-> ".messages [user]" - returns a number of messages sent in this channel by a '
                                  'particular user \n'
                                  '-> ".messages [channel]" - returns a number of messages in a mentioned channel \n'
                                  '-> ".messages [user] [channel]" or ".messages [channel] [user]" - returns a number '
                                  'of messages sent in a mentioned channel by a mentioned user')
    async def messages(self, ctx, user=None, channel=None):
        _user = user if checkforuser(user) else channel
        _channel = user if checkforchannel(user) else channel
        counter = 0
        if _user and _channel:
            channel = self.client.get_channel(int(_channel[2:-1]))
            async for message in channel.history(limit=None):
                if str(message.author.id) == str(_user)[3:-1]:
                    counter += 1
            if counter == 1:
                reply = "User {} sent {} message in the channel {}.".format(_user, counter, channel.mention)
            else:
                reply = "User {} sent {} messages in the channel {}.".format(_user, counter, channel.mention)
            await ctx.send(reply)
        elif _user:
            async for message in ctx.channel.history(limit=None):
                if str(message.author.id) == str(_user)[3:-1]:
                    counter += 1
            if counter == 1:
                reply = "User {} sent {} message in the channel {}.".format(_user, counter, ctx.channel.mention)
            else:
                reply = "User {} sent {} messages in the channel {}.".format(_user, counter, ctx.channel.mention)
            await ctx.send(reply)
        elif _channel:
            channel = self.client.get_channel(int(_channel[2:-1]))
            async for _ in channel.history(limit=None):
                counter += 1
            if counter == 1:
                reply = "There was {} message in the channel {}.".format(counter, channel.mention)
            else:
                reply = "There were {} messages in the channel {}.".format(counter, channel.mention)
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


def checkforuser(user_id):
    if not user_id:
        is_user = None
    elif user_id[1] == '@':
        is_user = True
    else:
        is_user = False

    return is_user


def checkforchannel(channel_id):
    if not channel_id:
        is_channel = None
    elif channel_id[1] == '#':
        is_channel = True
    else:
        is_channel = False

    return is_channel
