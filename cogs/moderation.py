import discord
from discord.ext import commands
import asyncio


class Moderations(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        await ctx.send(f'Error. Try help ({error})')
        print('error')
    
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self,ctx,amount=1):
        await ctx.channel.purge(limit=int(amount)+1)
        await ctx.send(f'I have deleted {amount} messages')
        await asyncio.sleep(2)
        await ctx.channel.purge(limit=1)
    
    @clear.error
    async def clear_error(self,ctx,error):
        if isinstance(error,commands.MissingPermissions):
            await ctx.send("Sorry You dont have permissions to run this command")


    @commands.command()
    async def kick(self,ctx, member : discord.Member, * , reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'{member} has been kicked')

    @commands.command()
    async def ban(self,ctx,member : discord.Member, * ,reason = None):
        await member.ban(reason=reason)
        await ctx.send(f'{member} has been banned')

    @commands.command()
    async def unban(self,ctx, * ,member):
        banned_users = await ctx.guild.bans()
        member_name , member_discriminator = member.split('#')
        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name,user.discriminator) == (member_name,member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.name}#{user.discriminator}')
                return

def setup(client):
    client.add_cog(Moderations(client))