from discord.ext import commands
import time
import datetime


class Top(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name='top',
                      brief='Leaderboard of messages sent',
                      description='-> ".top" - returns a leaderboard of users with the most messages sent in '
                                  'this channel \n'
                                  '-> ".top all" - returns a leaderboard of users with the most messages in a current '
                                  'server \n'
                                  '-> ".top [channel] - returns a leaderboard of users with the most messages sent in '
                                  'a mentioned channel \n'
                                  '-> ".top [channel] [limit]" - returns a limited leaderboard of users with the most '
                                  'messages sent in a mentioned channel \n')
    async def top(self, ctx, channel=None, limit=None):
        try:
            limit = int(limit)
        except ValueError and TypeError:
            limit = False

        messages = []
        members = set()
        results = []

        start = time.time()
        print('Executing...')

        if channel == 'all':
            await ctx.send(":warning: Warning! If you server is large enough,"
                           " calculations could take few hours. :warning: ")
            for _channel in ctx.guild.text_channels:
                async for message in _channel.history(limit=None):
                    if message.author.bot is not True:
                        members.add(message.author.id)
                        messages.append(message.author.id)
        else:
            _channel = self.client.get_channel(int(channel[2:-1])) if channel else ctx.channel

            async for message in _channel.history(limit=None):
                if message.author.bot is not True:
                    members.add(message.author.id)
                    messages.append(message.author.id)
        for member in members:
            counter = messages.count(member)
            try:
                results.append([member, counter, self.client.get_user(member).name,
                                self.client.get_user(member).discriminator])
            except AttributeError:
                pass

        results = sorted(results, key=lambda x: x[1], reverse=True)
        limit = int(limit) if (limit and 0 < int(limit) < len(results) and type(int(limit)) == int) else len(results)

        messages = create_message(ctx, results, channel, _channel, '', limit)

        end = time.time()
        print('Finished. Time of execution: {} seconds.'.format(round(end - start, 2)))

        for message in messages:
            await ctx.send(message)

    @commands.command(name='dailytop',
                      brief='Leaderboard of messages sent today',
                      description='-> ".dailytop" - returns a leaderboard of users with the most messages sent today '
                                  'in this channel \n'
                                  '-> ".dailytop all" - returns a leaderboard of users with the most messages sent '
                                  'today in a current server \n'
                                  '-> ".dailytop [channel] - returns a leaderboard of users with the most messages '
                                  'sent today in a mentioned channel \n'
                                  '-> ".dailytop [channel] [limit]" - returns a limited leaderboard of users with the '
                                  'most messages sent today in a mentioned channel \n')
    async def dailytop(self, ctx, channel=None, limit=None):
        try:
            limit = int(limit)
        except ValueError and TypeError:
            limit = False

        messages = []
        members = set()
        results = []

        start = time.time()
        print('Executing...')

        if channel == 'all':
            for _channel in ctx.guild.text_channels:
                async for message in _channel.history(limit=None):
                    if message.created_at > datetime.datetime.today().replace(hour=0, minute=0, second=0):
                        if message.author.bot is not True:
                            members.add(message.author.id)
                            messages.append(message.author.id)
                    else:
                        break
        else:
            _channel = self.client.get_channel(int(channel[2:-1])) if channel else ctx.channel

            async for message in _channel.history(limit=None):
                if message.created_at > datetime.datetime.today().replace(hour=0, minute=0, second=0):
                    if message.author.bot is not True:
                        members.add(message.author.id)
                        messages.append(message.author.id)
                else:
                    break

        for member in members:
            counter = messages.count(member)
            try:
                results.append([member, counter, self.client.get_user(member).name,
                                self.client.get_user(member).discriminator])
            except AttributeError:
                pass

        results = sorted(results, key=lambda x: x[1], reverse=True)
        limit = int(limit) if (limit and 0 < int(limit) < len(results) and type(int(limit)) == int) else len(
            results)

        messages = create_message(ctx, results, channel, _channel, 'today', limit)

        end = time.time()
        print('Finished. Time of execution: {} seconds.'.format(round(end - start, 2)))

        for message in messages:
            await ctx.send(message)


def setup(client):
    client.add_cog(Top(client))


def create_message(ctx, results, channel, _channel, period, limit=None):
    messages = []
    if channel == 'all':
        reply = ":trophy: ** Most messages sent **in {} {} :trophy: \n ".format(ctx.guild.name, period)
    else:
        reply = ":trophy: ** Most messages sent **in {} {} :trophy: \n ".format(_channel.mention, period)

    for i in range(limit):
        if i == 0:
            place = ':first_place: '
        elif i == 1:
            place = ':second_place: '
        elif i == 2:
            place = ':third_place: '
        else:
            place = '  ' + str(i + 1) + '.  '
        reply += '\n' + place + str(results[i][2]) + '#' + str(results[i][3]) + ' - **' + str(results[i][1]) + '**'

        if len(reply) > 1500:
            messages.append(reply)
            reply = ''

    return messages if len(messages) != 0 else [reply]
