import discord
from discord.ext import commands,tasks
from itertools import cycle
import os
import json

#to_get_prefix
def get_prefix(client,message):
    with open('prefixes.json','r') as f:
        prefixes = json.load(f)
    return prefixes[str(message.guild.id)]

#setting prefix
client = commands.Bot(command_prefix=get_prefix)
client.remove_command('help')

#status for bot to loop through
#status = cycle(['With OniiChan PP','Yamete OniiChan','OniiChan Just touched my nono part'])

#setting prefix while joining server
@client.event
async def on_guild_join(guild):
    with open('prefixes.json','r') as f:
        prefixes = json.load(f)
    
    prefixes[str(guild.id)] = '/'

    with open('prefixes.json','w') as f:
        json.dump(prefixes,f,indent=4)

#removing prefix while leaving server
@client.event
async def on_guild_remove(guild):
    with open('prefixes.json','r') as f:
        prefixes = json.load(f)
    prefixes.pop(str(guild.id))
    with open('prefixes.json','w') as f:
        json.dump(prefixes,f,indent=4)

#changing server prefix through command
@client.command()
async def changeprefix(ctx,prefix):
    with open('prefixes.json','r') as f:
        prefixes = json.load(f)
    prefixes[str(ctx.guild.id)] = prefix
    
    with open('prefixes.json','w') as f:
        json.dump(prefixes,f,indent=4)

    await ctx.send(f'Prefix has been changed to {prefix}')
  
@client.command()
async def datasteal(ctx):
    with open('prefixes.json','r') as f:
        prefixes = json.load(f)

        await ctx.send(prefixes)

#making bot do stufs when it is online
@client.event
async def on_ready():
    print("starto")
    await client.change_presence(status=discord.Status.idle,activity=discord.Game("I had a dream It was dark and I Couldnt breathe"))



#to make bot change status every mentioned seconds
# @tasks.loop(seconds=5)
# async def status_changer():
#     await client.change_presence(status=discord.Status.idle,activity=discord.Game(next(status)))

#say
@client.command()
async def say(ctx,*,sentence):
    await ctx.channel.purge(limit=1)
    await ctx.send(sentence)
    
@client.command()
async def load(ctx,extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} has been loaded')

@client.command()
async def unload(ctx,extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} has been unloaded')

@client.command()
async def reload(ctx,extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} has been reloaded')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

end = "token"

client.run(os.environ['DISCORD_TOKEN'])


