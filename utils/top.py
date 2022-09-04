from discord.ext import commands
from utils.functions import check_for_channel
from datetime import datetime, timedelta


NOW = datetime.now()
LOOKUP_DAYS = {'today': NOW.replace(hour=0, minute=0, second=0),
               'yesterday': NOW.replace(hour=0, minute=0, second=0) - timedelta(days=1),
               'week': NOW - timedelta(days=7),
               'month': NOW - timedelta(days=31),
               'year': NOW - timedelta(days=365),
               'all': NOW - timedelta(days=7*365)}


class Top(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name='top',
                      brief='Leaderboard of messages sent',
                      description='-> ".top" - returns a leaderboard of users with the most messages sent in '
                                  'this channel \n'
                                  '-> ".top [channel] [time] [limit]" - returns a limited leaderboard of users with '
                                  'the most messages sent in a mentioned channel \n'
                                  ' \n'
                                  '[time] = [today|week|month|year|all]')
    async def top(self, ctx, *args):
        messages, members, results = [], set(), []  # variables to collect and keep information
        _channel, limit, lookup_type = None, None, None  # details about query

        for arg in args:
            if check_for_channel(arg):
                _channel = arg
            if arg.isdigit():
                limit = int(arg)
            if arg in LOOKUP_DAYS:
                lookup_type = arg

        lookup_type = 'all' if lookup_type is None else lookup_type
        channel = self.client.get_channel(int(_channel[2:-1])) if _channel else ctx.channel
        async for message in channel.history(limit=None):
            message_time = message.created_at + timedelta(hours=2)
            if lookup_type != 'yesterday':
                if message_time > LOOKUP_DAYS[lookup_type]:
                    if message.author.bot is not True:
                        members.add(message.author.id)
                        messages.append(message.author.id)
                else:  # break if message was sent previous than lookup time
                    break
            else:
                if LOOKUP_DAYS[lookup_type] < message_time < LOOKUP_DAYS['today']:
                    if message.author.bot is not True:
                        members.add(message.author.id)
                        messages.append(message.author.id)
                elif LOOKUP_DAYS[lookup_type] > message_time:  # break if message was sent previous than lookup time
                    break

        for member in members:
            counter = messages.count(member)
            try:
                results.append([member, counter, self.client.get_user(member).name,
                                self.client.get_user(member).discriminator])
            except AttributeError:
                pass

        results = sorted(results, key=lambda x: x[1], reverse=True)
        limit = int(limit) if (limit and 0 < int(limit) < len(results) and type(int(limit)) == int) else len(results)

        messages = create_message(ctx, results, _channel, channel, lookup_type, limit)

        for message in messages:
            await ctx.send(message)


async def setup(client):
    await client.add_cog(Top(client))


def create_message(ctx, results, channel, _channel, period, limit=None):
    messages = []
    period = 'all-time' if period == 'all' else period
    period = 'last ' + period if period not in ['all-time', 'today', 'yesterday'] else period
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
