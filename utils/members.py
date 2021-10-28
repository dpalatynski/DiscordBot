from discord.ext import commands
from discord import Embed, Member


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
        else:
            reply = 'There are **{}** members of {}.'.format(len(ctx.guild.members), ctx.guild)

        embed = Embed(color=0x2ca5f1)
        embed.add_field(name="Members", value=reply)

        await ctx.send(embed=embed)

    @members.error
    async def members_eror(self, ctx, error):
        if error:
            embed = Embed(color=0xff0000)
            embed.add_field(name='Error', value=':no_entry: I can\'t count the number of members right now.')

            await ctx.send(embed=embed)

    @commands.command(name='user',
                      brief='Who are you?',
                      description='-> ".user " - information about your Discord account \n'
                                  '-> ".user [user]" - information about specific Discord account')
    async def user(self, ctx, user: Member = None):
        if user is None:
            user = ctx.message.author
        embed = Embed(title=user.display_name, color=0x2ca5f1)
        embed.set_thumbnail(url=user.avatar_url)
        embed.add_field(name='Nickname', value=user.name + '#' + user.discriminator, inline=False)
        embed.add_field(name='Joined At', value=user.joined_at.date())
        embed.add_field(name='Created At', value=user.created_at.date())
        embed.add_field(name='Roles:', value=get_roles(user.roles), inline=False)
        if user.premium_since is not None:
            embed.add_field(name=':gem: Server Boosting since:', value=user.premium_since.date())
        if len(user.activities) != 0:
            embed.add_field(name='Activites:', value=get_activities(user.activities), inline=False)
        embed.set_footer(text='User ID: ' + str(user.id))

        await ctx.send(embed=embed)

    @user.error
    async def user_eror(self, ctx, error):
        if error:
            embed = Embed(color=0xff0000)
            embed.add_field(name='Error', value=':no_entry: Unable to find information about this account.')

            await ctx.send(embed=embed)

    @commands.command(name='avatar',
                      brief='View an avatar',
                      description='-> ".avatar " - look at your Discord avatar \n'
                                  '-> ".avatar [user]" - look at user\'s Discord avatar')
    async def avatar(self, ctx, user: Member = None):
        if user is None:
            user = ctx.message.author
        embed = Embed(title=user.display_name, color=0x2ca5f1)
        embed.set_image(url=user.avatar_url)
        embed.set_footer(text=user.name + '#' + user.discriminator)

        await ctx.send(embed=embed)

    @avatar.error
    async def avatar_eror(self, ctx, error):
        if error:
            embed = Embed(color=0xff0000)
            embed.add_field(name='Error', value=':no_entry: Unable to look at this avatar.')

            await ctx.send(embed=embed)

    @commands.command(name='roles',
                      brief='Shows names of all roles',
                      description='-> ".roles " - returns names of all roles \n')
    async def roles(self, ctx):
        roles = get_roles(ctx.guild.roles)
        embed = Embed(title='Roles: ', description=roles.replace(',', '\n'), color=0x2ca5f1)

        await ctx.send(embed=embed)

    @roles.error
    async def roles_eror(self, ctx, error):
        if error:
            embed = Embed(color=0xff0000)
            embed.add_field(name='Error', value=':no_entry: Unable to display roles.')

            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Members(client))


def get_roles(roles):
    message = ''
    if len(roles) != 0:
        for role in roles[1:]:
            message += role.name + ', '
    else:
        message = 'No roles assigned!!!'

    return message[:-2]


def get_activities(activities):
    message = ''
    for activity in activities:
        if hasattr(activity, 'track_id'):
            message += ':headphones:  Listening: ' + activity.artist + ' - ' + activity.title + ' on Spotify \n'
        if hasattr(activity, 'application_id'):
            message += ':video_game:  Playing: ' + activity.name + ' \n'

    return message
