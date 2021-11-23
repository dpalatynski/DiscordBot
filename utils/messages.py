from discord.ext import commands
from discord import Embed


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
        elif _user:
            async for message in ctx.channel.history(limit=None):
                if str(message.author.id) == str(_user)[3:-1]:
                    counter += 1
            if counter == 1:
                reply = "User {} sent {} message in the channel {}.".format(_user, counter, ctx.channel.mention)
            else:
                reply = "User {} sent {} messages in the channel {}.".format(_user, counter, ctx.channel.mention)
        elif _channel:
            channel = self.client.get_channel(int(_channel[2:-1]))
            async for _ in channel.history(limit=None):
                counter += 1
            if counter == 1:
                reply = "There was {} message in the channel {}.".format(counter, channel.mention)
            else:
                reply = "There were {} messages in the channel {}.".format(counter, channel.mention)
        else:
            async for _ in ctx.channel.history(limit=None):
                counter += 1
            if counter == 1:
                reply = "There was {} message in the channel {}.".format(counter, ctx.channel.mention)
            else:
                reply = "There were {} messages in the channel {}.".format(counter, ctx.channel.mention)

        embed = Embed(color=0x2ca5f1)
        embed.add_field(name="Messages", value=reply)

        await ctx.send(embed=embed)

    @messages.error
    async def messages_eror(self, ctx, error):
        if error:
            embed = Embed(color=0xff0000)
            embed.add_field(name='Error', value=':no_entry: I can\'t count the number of messages right now.')

            await ctx.send(embed=embed)

    @commands.command(name='poll',
                      pass_context=True)
    async def poll(self, ctx, *args):
        numbers = {1: '1️⃣', 2: '2️⃣', 3: '3️⃣', 4: '4️⃣', 5: '5️⃣', 6: '6️⃣', 7: '7️⃣', 8: '8️⃣', 9: '9️⃣'}
        context = '{}'.format('"'.join(args))
        question = context.split('"')[0]
        answers = context.split('"')[1:]
        answer_message = create_answers(answers)
        embed = Embed(title=question, description=answer_message, color=0x2ca5f1)
        message = await ctx.send(embed=embed)
        for i in range(1, int(len(answers))+1):
            await message.add_reaction(numbers[i])


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


def create_answers(answers):
    answer = ''
    numbers = {1: '1️⃣', 2: '2️⃣', 3: '3️⃣', 4: '4️⃣', 5: '5️⃣', 6: '6️⃣', 7: '7️⃣', 8: '8️⃣', 9: '9️⃣'}
    for i in range(len(answers)):
        answer += f'{numbers[i+1]}: {answers[i]} \n \n'

    return answer[:-4]
