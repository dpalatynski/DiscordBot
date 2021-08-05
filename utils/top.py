from discord.ext import commands
import time


class Top(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name='top',
                      brief='TBA',
                      description='TBA',
                      aliases=[])
    async def top(self, ctx):
        start = time.time()
        print('Executing...')

        messages = []
        members = set()
        results = []
        async for message in ctx.channel.history(limit=None):
            members.add(message.author.id)
            messages.append(message.author.id)

        for member in members:
            counter = messages.count(member)
            results.append([member, counter])

        results = sorted(results, key=lambda x: x[1], reverse=True)

        reply = ":trophy: ** Most messages sent **in {} :trophy: \n ".format(ctx.channel.mention)
        for i in range(len(results)):
            if i == 0:
                place = ':first_place:'
            elif i == 1:
                place = ':second_place:'
            elif i == 2:
                place = ':third_place:'
            else:
                place = '  ' + str(i+1) + '. '
            reply += '\n' + place + str(self.client.get_user(results[i][0])) + ' - **' + str(results[i][1]) + '**'

        end = time.time()

        print('Finished. Time of execution: {} seconds.'.format(round(end-start, 2)))
        await ctx.send(reply)


def setup(client):
    client.add_cog(Top(client))
