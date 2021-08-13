from discord.ext import commands
import time


class Top(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name='top',
                      brief='Leaderboard of messages sent',
                      description='-> ".top" - returns a leaderboard of users with the most messages sent in '
                                  'this channel \n'
                                  '-> ".top [channel] - returns a leaderboard of users with the most messages sent in '
                                  'a mentioned channel \n'
                                  '-> ".top [channel] [limit]" - returns a limited leaderboard of users with the most '
                                  'messages sent in a mentioned channel')
    async def top(self, ctx, channel=None, limit=None):
        try:
            limit = int(limit)
        except ValueError and TypeError:
            limit = False

        channel = self.client.get_channel(int(channel[2:-1])) if channel else ctx.channel

        start = time.time()
        print('Executing...')

        messages = []
        members = set()
        results = []
        async for message in channel.history(limit=None):
            members.add(message.author.id)
            messages.append(message.author.id)

        for member in members:
            counter = messages.count(member)
            results.append([member, counter])

        results = sorted(results, key=lambda x: x[1], reverse=True)
        limit = int(limit) if (limit and 0 < int(limit) < len(results) and type(int(limit)) == int) else len(results)

        reply = ":trophy: ** Most messages sent **in {} :trophy: \n ".format(channel.mention)
        for i in range(limit):
            if i == 0:
                place = ':first_place:'
            elif i == 1:
                place = ':second_place:'
            elif i == 2:
                place = ':third_place:'
            else:
                place = '  ' + str(i + 1) + '.  '
            reply += '\n' + place + str(self.client.get_user(results[i][0])) + ' - **' + str(results[i][1]) + '**'

            if len(reply) > 1500:
                await ctx.send(reply)
                reply = ''

        end = time.time()
        print('Finished. Time of execution: {} seconds.'.format(round(end-start, 2)))

        await ctx.send(reply)


def setup(client):
    client.add_cog(Top(client))
