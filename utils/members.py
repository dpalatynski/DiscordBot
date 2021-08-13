from discord.ext import commands


class Members(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name='members',
                      brief='How many server members are there?',
                      description='-> ".members" - returns a number of members \n'
                                  '-> ".members show" - prints all usernames')
    async def members(self, ctx, show=None):
        if show == 'show':
            members_list = []
            for member in ctx.guild.members:
                members_list.append(str(member))
            reply = '\n'.join(sorted(members_list))
        elif show:
            reply = 'Do you mean ".members" or ".members show"?'
        else:
            reply = 'There are {} members of {}.'.format(len(ctx.guild.members), ctx.guild)

        await ctx.send(reply)


def setup(client):
    client.add_cog(Members(client))
