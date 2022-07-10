import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(intents=intents, command_prefix='mimi ')

allowlist = 970755295942963200
wl = 983367913706774589
smulip = 940207773185105962
kitten = 900810644561997885
dead = 976680040098062387
testsorvor = 744107902587109396
whitelisted_kitten = 901054830540386354

@client.command()
@commands.has_permissions(manage_roles=True)
async def gib(ctx, role: discord.Role):
    left_over = []
    successful = []
    await ctx.send("Reply with discord usernames (follow the format)")

    def check(m):
        return m.author.id == ctx.author.id

    message = await client.wait_for('message', check=check, timeout=120)
    await ctx.send("on it :cat:")

    msg = message.content
    username_list = msg.split('\n')
    for username in username_list:
        username = username.rstrip()
        try:
            namez, id = username.split('#')
        except:
            left_over.append(username)

        user = discord.utils.get(ctx.guild.members, name=namez, discriminator=id)
        if user == None:
            left_over.append(username)
        else:
            await user.add_roles(role)
            successful.append(username)
    wled = "**Successful**"
    for i in successful:
        wled = wled + "\n" + i
    nwled = "**Not Found**"
    for i in left_over:
        nwled = nwled + "\n" + i

    await ctx.send(wled)
    await ctx.send(nwled)
    
        
# @client.event
# async def on_command_error(ctx, error):
#     # if command has local error handler, return
#     if hasattr(ctx.command, 'on_error'):
#         return
#
#     # get the original exception
#     error = getattr(error, 'original', error)
#
#     if isinstance(error, commands.CommandNotFound):
#         await ctx.send("Command doesnt exist")
#         return
#
#     if isinstance(error, commands.BotMissingPermissions):
#         missing = [perm.replace('_', ' ').replace('guild', 'server').title() for perm in error.missing_perms]
#         if len(missing) > 2:
#             fmt = '{}, and {}'.format("**, **".join(missing[:-1]), missing[-1])
#         else:
#             fmt = ' and '.join(missing)
#         _message = 'I need the **{}** permission(s) to run this command.'.format(fmt)
#         await ctx.send(_message)
#         return
#
#     if isinstance(error, commands.MissingPermissions):
#         missing = [perm.replace('_', ' ').replace('guild', 'server').title() for perm in error.missing_perms]
#         if len(missing) > 2:
#             fmt = '{}, and {}'.format("**, **".join(missing[:-1]), missing[-1])
#         else:
#             fmt = ' and '.join(missing)
#         _message = 'You need the **{}** permission(s) to use this command.'.format(fmt)
#         await ctx.send(_message)
#         return
#
#
#     if isinstance(error, commands.CheckFailure):
#         await ctx.send("You do not have permission to use this command.")
#         return
#
#     # ignore all other exception types, but print them to stderr
#     print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
#
#     if isinstance(error, commands.CheckFailure):
#         await ctx.send("You do not have permission to use this command.")
#         return
#
#     # ignore all other exception types, but print them to stderr
#     print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)

# @client.command()
# async def replace(ctx, role: discord.Role, role2: discord.Role):
#     left_over = []
#     successful = []
#     await ctx.send("Doing...")
#     i = 0

#     username_list = open('successful_users.txt', encoding='utf-8').read().splitlines()
#     # guild = client.get_guild(744107902587109396)
#     for user_id in username_list:
#         user = ctx.guild.get_member(int(user_id))
#         if user == None:
#             left_over.append(user_id)
#         else:
#             await user.remove_roles(role)
#             await user.add_roles(role2)
#             print(f"Done For {user}")
#             i = i + 1
#             print(i)
#             successful.append(user_id)

#     with open('succesful.txt','w',encoding='utf-8') as f:
#         for temp in successful:
#             f.write(f'{str(temp)}\n')
#     with open('left_over.txt','w',encoding='utf-8') as f:
#         for temp in left_over:
#             f.write(f'{str(temp)}\n')
#     await ctx.send(f"Successfully done for {len(successful)} users")
#     await ctx.send(f"Couldn't find {len(left_over)} users")


   
@client.event
async def on_raw_reaction_add(payload):
    if payload.channel_id == 900819054053449769:
        channel = client.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        user = client.get_user(payload.user_id)
        await message.remove_reaction('🤡',user)
 
@client.command()
@commands.has_permissions(manage_roles=True)
async def assign(ctx,role:discord.Role):
    if ctx.message.reference:
        message = await ctx.fetch_message(id=ctx.message.reference.message_id)
    else:
        message_id = 991908762992513064
        message = await ctx.fetch_message(id=message_id)
    await ctx.send("on it :cat:")
    left_over = []
    successful = []
    for item in message.content.split(" "):
        # print(item)
        temp = ""
        if item.startswith('<@'):
            for i in item:
                if i.isdigit():
                    temp = temp + i
            user = ctx.guild.get_member(int(temp))
            if user == None:
                left_over.append(str(user))
            else:
                await user.add_roles(role)
                successful.append(str(user))
    await ctx.send(f"Successfully done for {len(successful)} users")
    await ctx.send(f"Couldn't find {len(left_over)} users")

@client.command()
async def list(ctx):
    if ctx.message.reference:
        message = await ctx.fetch_message(id=ctx.message.reference.message_id)
    else:
        await ctx.send("Please reply to the message")
        message_id = 991908762992513064
        message = await ctx.fetch_message(id=message_id)
    await ctx.send("on it :cat:")
    left_over = []
    successful = []
    author_list = []
    for item in message.content.split(" "):
        temp = ""
        if item.startswith('<@'):
            for i in item:
                if i.isdigit():
                    temp = temp + i
            user = ctx.guild.get_member(int(temp))
            if user == None:
                left_over.append(str(user))
            else:
                author_list.append((user.name + '#' + str(user.discriminator)))
                successful.append(str(user.id))
    msg = "**Usernames**\n"
    for user in author_list:
        msg = msg + user + "\n"
    await ctx.author.send(msg)
    msg = "**UserIDs**\n"
    for user_id in successful:
        msg = msg + user_id + "\n"
    await ctx.author.send(msg)
    await ctx.send(f"Check DM")

@client.event
async def on_message(message):
    # print(message.author)
    if message.guild.id == 989976603243188224:
        princes = 990559906065182781
        holders = 995499325473947648
        prince = message.guild.get_role(princes)
        holder = message.guild.get_role(holders)
        user = message.author
        if not prince in user.roles:
            links = [".com", ".net", ".org", ".co", ".us", ".ml", ".tk", ".ga", ".cf", ".gq", "https","PHASE 2 MINTING LIVE NOW"]
            white = ["tenor"]
            if any(word in message.content.lower() for word in links) and any(
                    word not in message.content.lower() for word in white):
                await message.delete() 
   
client.run(os.environ["DISCORD_TOKEN"])

