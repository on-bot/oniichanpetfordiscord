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
async def customgib(ctx,role:discord.Role):
    role2_id = allowlist
    guild_id = smulip
    guild = client.get_guild(guild_id)
    role2 = discord.utils.get(guild.roles, id=role2_id)
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
            if role2 in user.roles:
                await user.remove_roles(role2)
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

@client.command()
async def forgib(ctx):
    await ctx.send("Too late wallet submission is closed. Try premint raffle")

@client.command()
async def check(ctx,wallet):
    wallets = open('wallets.txt', encoding='utf-8').read().splitlines()
    wallets = [wallet for wallet.lower in wallets]
    if wallet.lower in wallets:
        await ctx.message.add_reaction('✅')
    else:
        await ctx.message.add_reaction('❌')

client.run(os.environ["DISCORD_TOKEN"])

