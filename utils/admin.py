from discord.ext import commands
from discord import Embed
from discord.utils import get


class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name='createrole',
                      brief='Create new role',
                      description='-> ".createrole" - creates a new role')
    async def createrole(self, ctx, *role_name):
        new_role = " ".join(role_name) if len(role_name) != 0 else "new role"
        await ctx.guild.create_role(name=new_role)
        embed = Embed(color=0x2ca5f1)
        embed.add_field(name='Done!', value='Role %s has been created' % new_role)

        await ctx.send(embed=embed)

    @createrole.error
    async def createrole_eror(self, ctx, error):
        if isinstance(error, commands.errors.MissingRequiredArgument):
            embed = Embed(color=0xff0000)
            embed.add_field(name='Warning', value=':warning: Please specify the name of new role')
        else:
            embed = Embed(color=0xff0000)
            embed.add_field(name='Error', value=':no_entry: I\'m unable to create a new role')

        await ctx.send(embed=embed)

    @commands.command(name='deleterole',
                      brief='Delete existing role',
                      description='-> ".deleterole" - deletes an existing role',
                      pass_context=True)
    async def deleterole(self, ctx, *role_name):
        if role_name[0][0] == '<':
            role = ctx.guild.get_role(int(role_name[0][3:-1]))
        else:
            role_name = " ".join(role_name)
            role = get(ctx.message.guild.roles, name=role_name)
        await role.delete()
        embed = Embed(color=0x2ca5f1)
        embed.add_field(name='Done!', value='Role %s has been deleted' % role)
        await ctx.send(embed=embed)

    @deleterole.error
    async def deleterole_eror(self, ctx, error):
        if isinstance(error, commands.errors.MissingRequiredArgument):
            embed = Embed(color=0xff0000)
            embed.add_field(name='Warning', value=':warning: Please specify the name of the role')
        else:
            embed = Embed(color=0xff0000)
            embed.add_field(name='Error', value=':no_entry: I\'m unable to delete this role')

        await ctx.send(embed=embed)

    @commands.command(name='deletemessages',
                      brief='Delete last [number] messages',
                      description='-> ".delemessages [number]" - deletes a specified number of messages in '
                                  'current channel')
    @commands.has_permissions(administrator=True)
    async def deletemessages(self, ctx, number):
        if int(number) > 10:
            embed = Embed(color=0xff0000)
            embed.add_field(name='Warning', value=':no_entry: You can\'t delete more than 10 messages.')

            await ctx.send(embed=embed)
        else:
            async for message in ctx.channel.history(limit=int(number)):
                await message.delete()

    @deletemessages.error
    async def deletemessages_eror(self, ctx, error):
        if isinstance(error, commands.errors.MissingPermissions):
            embed = Embed(color=0xff0000)
            embed.add_field(name='Warning', value=':no_entry: You are missing Administrator permission to run this '
                                                  'command.')
        elif isinstance(error, commands.errors.MissingRequiredArgument):
            embed = Embed(color=0xff0000)
            embed.add_field(name='Warning', value=':warning: Please specify the number of messages to delete')
        else:
            embed = Embed(color=0xff0000)
            embed.add_field(name='Error', value=':no_entry: I\'m unable to delete messages')

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Admin(client))
