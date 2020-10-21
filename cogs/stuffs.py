import discord
from discord.ext import commands
import asyncio
from datetime import date


class Stuffs(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.command(pass_context=True)
    async def help(self,ctx):

        embed = discord.Embed(title="Add Prefix and Do commands below",colour = discord.Colour.green())
        embed.set_author(name="Commands Lists")
        embed.add_field(name='uhelp', value='Moderation tools', inline=False)
        embed.add_field(name='shelp', value='The thing I as a pet is capable of rn', inline=False)

        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def uhelp(self,ctx):
        embed = discord.Embed(title="Utility Help", colour=discord.Colour.red())
        embed.add_field(name='ban', value='Bans the user from server', inline=False)
        embed.add_field(name='unban', value='Unbans the banned user', inline=False)
        embed.add_field(name='kick', value='Kicks the user from server', inline=False)
        embed.add_field(name='clear', value='Deletes the specified number of messages', inline=False)

        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def shelp(self, ctx):
        embed = discord.Embed(title="Stuffs Help", colour=discord.Colour.purple())
        embed.add_field(name='dmafter', value='DMs You after the mentioned time(seconds)', inline=False)
        embed.add_field(name='dmstuffs', value='DMs the mentioned user the written messages <dmstuff @user message>', inline=False)
        embed.add_field(name='mentionafter',value='Mentions the mentioned user after specified time(seconds) <mentionafter time @user>',inline=False)
        embed.add_field(name='h2s', value='Converts hours into seconds', inline=False)
        embed.add_field(name='m2s', value='Converts minutes into seconds', inline=False)
        embed.add_field(name='todaydate', value='Shows Todays Date(IDK why i added this)', inline=False)

        await ctx.send(embed=embed)

    @commands.command()
    async def dmstuff(self,ctx, user: discord.User, *, message=None):
        message = message or "This Message is sent via DM"
        await user.send(message)

    @commands.command()
    async def dm(self,ctx, user: discord.User, timetomention):
        if timetomention.isnumeric():
            await ctx.send(f"Nyan Nyan! Goshujin-Sama I will dm you after {timetomention} seconds")
            await asyncio.sleep(int(timetomention))
            await user.send("It's time")
        else:
            await ctx.send("Input time in seconds")

    @commands.command()
    async def m2s(self,ctx,minutes):
        if minutes.isnumeric():
            seconds = int(minutes) * 60
            await ctx.send(f'{minutes} minutes is {seconds} seconds')
        else:
            await ctx.send("Are ya dumb?")

    @commands.command()
    async def mentionafter(self,ctx, timetomention,user: discord.User):
        if timetomention.isnumeric():
            await ctx.send(f"Nyan Nyan! Goshujin-Sama I will mention you after {timetomention} seconds")
            await asyncio.sleep(int(timetomention))
            await ctx.send(f"Moshi Moshi {user.mention} Soko ni imasuka?")
        else:
            await ctx.send("Input time in seconds dumbass")

    @commands.command()
    async def h2s(self,ctx,hours):
        if hours.isnumeric():
            seconds = int(hours) * 60 *60
            await ctx.send(f'{hours} hours is {seconds} seconds')
        else:
            await ctx.send("Are ya dumb?")
            
    @commands.command()
    async def todaydate(self,ctx):
        await ctx.send(date.today())
    
def setup(client):
    client.add_cog(Stuffs(client))