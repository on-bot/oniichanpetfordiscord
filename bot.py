import discord
from discord.ext import commands
from fileforlists import responses,url_giver,comment_and_name_shower,comments_and_username_list
import random
import time
from datetime import date
import asyncio

client = commands.Bot(command_prefix='`')

@client.event
async def on_ready():
    print("Onii-Chan Yamete!")
    await client.change_presence(status="Online",activity=discord.Game("With OniiChan PP"))


@client.event
async def on_member_join(member):
    print(f'{member} has joined the server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left the server')

@client.command()
async def ping(ctx):
    await ctx.send(f'OwO! {round(client.latency*1000)} ms')

@client.command(aliases=['guess','predict','say'])
async def Guess(ctx, *,question):
    await ctx.send(f'Question: {question}?\nAnswer: {random.choice(responses)}')

    
@client.command()
async def clear(ctx, amount=0):
    if (ctx.message.author.permissions_in(ctx.message.channel).manage_messages):
        await ctx.channel.purge(limit= amount+1)
        await ctx.send(f'I have deleted {amount} messages')
        time.sleep(2)
        await ctx.channel.purge(limit = 1)

@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('Sorry you are not allowed to use this command.')



@client.command() 
async def kick(ctx, member : discord.Member, * , reason=None): 
    await member.kick(reason=reason)
    await ctx.send(f'{member} has been kicked')

@client.command()
async def ban(ctx, member : discord.Member, * ,reason = None):
    await member.ban(reason=reason)
    await ctx.send(f'{member} has been banned')

@client.command()
async def unban(ctx, * ,member):
    banned_users = await ctx.guild.bans()
    member_name , member_discriminator = member.split('#')
    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name,user.discriminator) == (member_name,member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.name}#{user.discriminator}')
            return 

@client.command()
async def redditcomments(ctx,*,url,amount=5):
    try:
        url_giver(url)
        comment_and_name_shower()
        count = 0
        for one_comment in comments_and_username_list:
            await ctx.send(one_comment)
            count += 1
            if count == amount:
                break
    except:
        await ctx.send("Url isnt valid")

@client.command()
async def todaydate(ctx):
    await ctx.send(date.today())


@client.command()
async def dmstuff(ctx, user: discord.User, *, message=None):
    message = message or "This Message is sent via DM"
    await user.send(message)

@client.command()
async def dm(ctx, user: discord.User, timetomention):
    if timetomention.isnumeric():
        await ctx.send(f"Nyan Nyan! Goshujin-Sama I will dm you after {timetomention} seconds")
        await asyncio.sleep(int(timetomention))
        await user.send("It's time")
    else:
        await ctx.send("Input time in seconds")
    
@client.command()
async def sec2min(ctx,minutes):
    if minutes.isnumeric():
        seconds = int(minutes) * 60
        await ctx.send(f'{minutes} minutes is {seconds} seconds')
    else:
        await ctx.send("Are ya dumb?")


nk='NzYwMzMwMDIzNzc2'
bk='NDE5ODUw.X3Kegw.x8NfyLNv'
ck='oJnH0uk1uSPzsUZfkco ' 
    
endd=nk+bk+ck

client.run(endd)


