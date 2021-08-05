from discord.ext import commands


class Members(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name='members',
                      brief='TBA',
                      description='TBA',
                      aliases=[])
    async def members(self, ctx, show=None):
        if show == 'show':
            members_list = []
            for member in ctx.guild.members:
                members_list.append(str(member))
            reply = '\n'.join(sorted(members_list))
        else:
            reply = 'There are {} members of {}.'.format(len(ctx.guild.members), ctx.guild)

        await ctx.send(reply)


def setup(client):
    client.add_cog(Members(client))
