import os
import discord
import datetime
from discord.ext import commands
import sys
import requests
import re
import asyncio
import json
import random
from pymongo import MongoClient

intents = discord.Intents.all()
intents.members = True

# MONGO
command_list = ['mimi ','Mimi ']

client = commands.Bot(intents=intents, command_prefix=command_list)

cluster = MongoClient(os.environ['MONGO_TOKEN'])
db = cluster["discord"]
collection = db["ethos_xp_cat"]

client.remove_command('help')
allowlist = 970755295942963200
wl = 983367913706774589
smulip = 940207773185105962
kitten = 900810644561997885
dead = 976680040098062387
testsorvor = 744107902587109396
whitelisted_kitten = 901054830540386354


def check_list(list_1, list_2):
    for a in list_1:
        if a in list_2:
            return True
    return False


@client.command()
async def gib(ctx, role: discord.Role):
    if ctx.author.guild_permissions.manage_roles or ctx.author.id == 480361233049059338 or ctx.author.id == 776716251997274112:
        left_over = []
        successful = []
        await ctx.send("Reply with discord usernames (follow the format)")

        def check(m):
            return m.author.id == ctx.author.id

        message = await client.wait_for('message', check=check, timeout=120)
        if not message.author.bot:
            await ctx.send("on it :cat:")
            if message.attachments:
                attachment = message.attachments[0]
                url = attachment.url
                r = requests.get(url, allow_redirects=True)

                open('temp.txt', 'wb').write(r.content)
                username_list = open('temp.txt', encoding='utf-8').read().splitlines()
                os.remove("temp.txt")
            else:
                msg = message.content
                username_list = msg.split('\n')
            for username in username_list:
                username = username.rstrip()
                try:
                    namez, id = username.split('#')
                    user = discord.utils.get(ctx.guild.members, name=namez, discriminator=id)
                except:
                    user = None

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

            if len(wled) > 15 and len(wled) < 1900:
                await message.channel.send(wled)
            if len(nwled) > 14 and len(nwled) < 1900:
                await message.channel.send(nwled)
            await ctx.send(f"Successfully done for {len(successful)} users")
            await ctx.send(f"Couldn't find {len(left_over)} users")


@client.command()
async def ungib(ctx, role: discord.Role):
    if ctx.author.guild_permissions.manage_roles or ctx.author.id == 480361233049059338 or ctx.author.id == 776716251997274112:
        left_over = []
        successful = []
        await ctx.send("Reply with discord usernames (follow the format)")

        def check(m):
            return m.author.id == ctx.author.id

        message = await client.wait_for('message', check=check, timeout=120)
        if not message.author.bot:
            await ctx.send("on it :cat:")
            if message.attachments:
                attachment = message.attachments[0]
                url = attachment.url
                r = requests.get(url, allow_redirects=True)

                open('temp.txt', 'wb').write(r.content)
                username_list = open('temp.txt', encoding='utf-8').read().splitlines()
                os.remove("temp.txt")
            else:
                msg = message.content
                username_list = msg.split('\n')
            for username in username_list:
                username = username.rstrip()
                try:
                    namez, id = username.split('#')
                    user = discord.utils.get(ctx.guild.members, name=namez, discriminator=id)
                except:
                    user = None

                if user == None:
                    left_over.append(username)
                else:
                    await user.remove_roles(role)
                    successful.append(username)
            wled = "**Successful**"
            for i in successful:
                wled = wled + "\n" + i
            nwled = "**Not Found**"
            for i in left_over:
                nwled = nwled + "\n" + i

            if len(wled) > 15 and len(wled) < 1900:
                await message.channel.send(wled)
            if len(nwled) > 14 and len(nwled) < 1900:
                await message.channel.send(nwled)
            await ctx.send(f"Successfully done for {len(successful)} users")
            await ctx.send(f"Couldn't find {len(left_over)} users")


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
async def on_ready():
    await client.change_presence(activity=discord.Game(name="with mimi"))
    print("Bot is ready!")


# @client.event
# async def on_raw_reaction_add(payload):
#     channel = client.get_channel(payload.channel_id)
#     message = await channel.fetch_message(payload.message_id)
#     user = client.get_user(payload.user_id)
#     await message.remove_reaction('🤡', user)


@client.command()
async def assign(ctx, role: discord.Role):
    if ctx.message.reference:
        message = await ctx.fetch_message(ctx.message.reference.message_id)
    else:
        await ctx.send("Please reply to the message")
        message_id = 991908762992513064
        message = await ctx.fetch_message(message_id)
    for user in message.mentions:
        await user.add_roles(role)

    await ctx.send("Done")


@client.command()
async def list(ctx):
    if ctx.message.reference:
        message = await ctx.fetch_message(ctx.message.reference.message_id)
    else:
        await ctx.send("Please reply to the message")
        message_id = 991908762992513064
        message = await ctx.fetch_message(message_id)

    author_list = []
    successful = []
    for user in message.mentions:
        author_list.append(user.name + "#" + user.discriminator)
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


# @client.event
# async def on_message(message):
#     if message.guild.id == 995429222497652796:
#         princes = 995637756673933332
#         maleks = 995636894895460403
#         prince = message.guild.get_role(princes)
#         malek = message.guild.get_role(maleks)
#         user = message.author
#         if user == None:
#             print("no")
#         else:
#             if message.attachments:
#                 text = ''.join(str(e) for e in message.attachments)
#                 text = text[-3:]
#                 if text == "txt":
#                     await message.delete()
#                     return
#             if not prince in user.roles and not malek in user.roles:
#                 links = [".com", ".net", ".org", ".co", ".us", ".ml", ".tk", ".ga", ".cf", ".gq", "https",
#                          "PHASE 2 MINTING LIVE NOW", "http", "👉 http", "mint.io", "scam","𝘄𝘄𝘄.𝗯𝗶𝗹𝗹𝗶𝗼𝗻𝗮𝗶𝗿𝗲𝗯𝗶𝗿𝗱𝘀.𝗺𝗹","claim here","FAKE RAFFLE with 0 real winners. 200 checks in a row"]
#                 white = ["tenor"]
#                 if any(word in message.content.lower() for word in links) and any(
#                         word not in message.content.lower() for word in white):
#                     await message.delete()
#     if message.guild.id == 995429222497652796 and not message.author.bot:
#         if message.channel.id == 996666624058867774:
#             left_over = []
#             successful = []
#             username_list = message.content.split("\n")
#             role = message.guild.get_role(995639674104189010)
#             for username in username_list:
#                 username = username.rstrip()
#                 if username.startswith('<@'):
#                     user_id = ""
#                     for c in username:
#                         if c.isdigit():
#                             user_id = user_id + c
#                     user = message.guild.get_member(int(user_id))
#                 else:
#                     try:
#                         namez, id = username.split('#')
#                     except:
#                         continue
#                     user = discord.utils.get(message.guild.members, name=namez, discriminator=id)

#                 if user == None:
#                     left_over.append(username)
#                 else:
#                     await user.add_roles(role)
#                     successful.append(user.name + '#' + str(user.discriminator))
#             wled = "**Successful**"
#             for i in successful:
#                 wled = wled + "\n" + i
#             nwled = "**Not Found**"
#             for i in left_over:
#                 nwled = nwled + "\n" + i
#             if len(wled) > 15:
#                 await message.channel.send(wled)
#             if len(nwled) > 14:
#                 await message.channel.send(nwled)
#             await message.channel.send(f"Successfully done for {len(successful)} users")
#             await message.channel.send(f"Couldn't find {len(left_over)} users")

#     if message.guild.id == 995429222497652796 and not message.author.bot:
#         if message.channel.id == 999275777688346735:
#             left_over = []
#             successful = []
#             username_list = message.content.split("\n")
#             role = message.guild.get_role(999272311511339049)
#             for username in username_list:
#                 username = username.rstrip()
#                 if username.startswith('<@'):
#                     user_id = ""
#                     for c in username:
#                         if c.isdigit():
#                             user_id = user_id + c
#                     user = message.guild.get_member(int(user_id))
#                 else:
#                     try:
#                         namez, id = username.split('#')
#                     except:
#                         continue
#                     user = discord.utils.get(message.guild.members, name=namez, discriminator=id)

#                 if user == None:
#                     left_over.append(username)
#                 else:
#                     await user.add_roles(role)
#                     successful.append(user.name + '#' + str(user.discriminator))
#             wled = "**Successful**"
#             for i in successful:
#                 wled = wled + "\n" + i
#             nwled = "**Not Found**"
#             for i in left_over:
#                 nwled = nwled + "\n" + i
#             if len(wled) > 15:
#                 await message.channel.send(wled)
#             if len(nwled) > 14:
#                 await message.channel.send(nwled)
#             await message.channel.send(f"Successfully done for {len(successful)} users")
#             await message.channel.send(f"Couldn't find {len(left_over)} users")
#     await client.process_commands(message)


@client.event
async def on_message_edit(before, after):
    if after.guild.id == 989976603243188224:
        princes = 990241246222094366
        holders = 995499325473947648
        prince = after.guild.get_role(princes)
        holder = after.guild.get_role(holders)
        if before.content != after.content:
            links = [".com", ".net", ".org", ".co", ".us", ".ml", ".tk", ".ga", ".cf", ".gq", "https",
                     "PHASE 2 MINTING LIVE NOW"]
            white = ["tenor"]
            if any(word in after.content.lower() for word in links) and any(
                    word not in after.content.lower() for word in white):
                await after.delete()


@client.event
async def on_message_delete(message):
    if message.guild.id == 995429222497652796 and message.channel.id == 996666624058867774:
        channel = client.get_channel(997483582312427580)
        embed = discord.Embed(
            colour=discord.Colour.blue(),
            title=f"Deleted Message by {message.author.name + '#' + str(message.author.discriminator)}"
        )
        embed.add_field(name="Message:\n", value=message.content, inline=True)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text='\u200b')
        await channel.send(embed=embed)


@client.event
async def on_member_join(member):
    if member.guild.id == 995429222497652796:
        mods = ["emirrZ", "alhubu", "King Khalid", "Hakim CZ", "Khalifa Billionaire", "Brother Bill", "Aziz Trump",
                "Malek Salman",
                "princeomarr", "mochi chan", "𝗡𝗮𝗻𝗰𝘆 𝗮𝗷𝗿𝗮𝗺", "WeirdclownisSAD", "Nipherme",
                "Yakub A.B", "Greedisgood", "David Eth Lord",
                "haifa wehb", "Muhammad Bin Hakim", "Subarash", "amoudi", "Blessed EDDIE", "Rachel19", "Cheeze",
                "King Nasr", "King Khalid",
                "Malek Salman", "billionare bird", "billionare birds", "billionarebirds", "billionarebird"]
        if any(word.lower() in member.name.lower() for word in mods):
            await member.ban(reason="Impersonating mods")


# @client.command()
# async def clear(ctx, amount=1):
#     await ctx.message.delete()
#     await ctx.channel.purge(limit=amount+1)
#     await ctx.send(f"Deleted {amount} messages", delete_after=5)


@client.command()
async def help(ctx):
    if ctx.guild.id == 1039314094081183824:  # ethos
        valid = False
    else:
        valid = False

    if valid:
        help_e = discord.Embed(
            colour=discord.Colour.orange()
        )
        help_e.set_author(name="Bot prefix = mimi ")
        help_e.add_field(name="gib <Role>", value="It will give chosen role to the list of usernames", inline=False)
        help_e.add_field(name="ungib <Role>", value="It will remove chosen role from the list of usernames",
                         inline=False)
        help_e.add_field(name="assign <Role>",
                         value="Reply to the message with this command and it will give the chosen "
                               "role to all the mentioned users in the message", inline=False)
        help_e.add_field(name="list", value="Reply to the message with this command and it will dm you the "
                                            "userid and usernames of all the mentioned users in the message",
                         inline=False)
        help_e.add_field(name="check", value="Checks if the bot is online", inline=False)
        help_e.add_field(name="clear <num>", value="Deletes the specified number of messages", inline=False)
        await ctx.send(embed=help_e)


@client.command()
async def get_wallets(ctx):
    channel = ctx.channel
    messages = await channel.history(limit=1000).flatten()
    user_ids = []
    user_wallets = []
    user_names = []
    for message in messages:
        if message.content.startswith('0x') and message.author.id not in user_ids:
            user_ids.append(message.author.id)
            user_names.append(message.author.name + '#' + str(message.author.discriminator))
            user_wallets.append(message.content)
    user_ids.reverse()
    user_wallets.reverse()
    user_names.reverse()
    with open("user_ids.txt", 'w', encoding='utf-8') as f:
        for user in user_ids:
            f.write(str(user) + '\n')

    with open("user_names.txt", 'w', encoding='utf-8') as f:
        for user in user_names:
            f.write(str(user) + '\n')

    with open("wallets.txt", 'w', encoding='utf-8') as f:
        for wallet in user_wallets:
            f.write(str(wallet) + '\n')

    file = discord.File("user_ids.txt")
    await ctx.send(file=file, content="IDs of Users")
    os.remove('user_ids.txt')
    file = discord.File("user_names.txt")
    await ctx.send(file=file, content="Usernames")
    os.remove('user_names.txt')
    file = discord.File("wallets.txt")
    await ctx.send(file=file, content="Wallets")
    os.remove('wallets.txt')


async def check_roles(guild, user_id, invite):
    check_dict = {}
    user = guild.get_member(int(user_id))
    if user is None:
        return
    check_dict[5] = 1033581489796939836
    check_dict[15] = 1033581373925109912
    check_dict[30] = 1033581350420226089
    check_dict[50] = 1033581274176163841
    check_dict[100] = 1033581189929369670
    check_dict[200] = 1033581096765493349
    check_dict[400] = 1033612000913276959
    if invite == 5:
        await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[400]))
        await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[200]))
        await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[100]))
        await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[50]))
        await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[30]))
        await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[15]))
        await user.add_roles(discord.utils.get(guild.roles, id=check_dict[5]))
    elif invite == 15:
        await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[400]))
        await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[200]))
        await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[100]))
        await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[50]))
        await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[30]))
        await user.add_roles(discord.utils.get(guild.roles, id=check_dict[15]))
        await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[5]))
    elif invite == 30:
        await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[400]))
        await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[200]))
        await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[100]))
        await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[50]))
        await user.add_roles(discord.utils.get(guild.roles, id=check_dict[30]))
        await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[15]))
        await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[5]))
    elif invite == 50:
        await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[400]))
        await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[200]))
        await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[100]))
        await user.add_roles(discord.utils.get(guild.roles, id=check_dict[50]))
        await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[30]))
        await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[15]))
        await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[5]))
    elif invite == 100:
        await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[400]))
        await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[200]))
        await user.add_roles(discord.utils.get(guild.roles, id=check_dict[100]))
        await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[50]))
        await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[30]))
        await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[15]))
        await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[5]))
    elif invite == 200:
        await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[400]))
        await user.add_roles(discord.utils.get(guild.roles, id=check_dict[200]))
        await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[100]))
        await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[50]))
        await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[30]))
        await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[15]))
        await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[5]))
    elif invite == 400:
        await user.add_roles(discord.utils.get(guild.roles, id=check_dict[400]))
        await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[200]))
        await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[100]))
        await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[50]))
        await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[30]))
        await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[15]))
        await user.remove_roles(discord.utils.get(guild.roles, id=check_dict[5]))


async def give_role(name, disc, invites):
    totalInvites = invites
    guild = client.get_guild(989976603243188224)
    user = discord.utils.get(guild.members, name=name, discriminator=disc)
    if totalInvites >= 400:
        five_invites_role = discord.utils.get(guild.roles, id=1033612000913276959)
        await user.add_roles(five_invites_role)
        await check_roles(guild, user.id, 400)
    elif totalInvites >= 200:
        five_invites_role = discord.utils.get(guild.roles, id=1033581096765493349)
        await user.add_roles(five_invites_role)
        await check_roles(guild, user.id, 200)
    elif totalInvites >= 100:
        five_invites_role = discord.utils.get(guild.roles, id=1033581189929369670)
        await user.add_roles(five_invites_role)
        await check_roles(guild, user.id, 100)
    elif totalInvites >= 50:
        five_invites_role = discord.utils.get(guild.roles, id=1033581274176163841)
        await user.add_roles(five_invites_role)
        await check_roles(guild, user.id, 50)
    elif totalInvites >= 30:
        five_invites_role = discord.utils.get(guild.roles, id=1033581350420226089)
        await user.add_roles(five_invites_role)
        await check_roles(guild, user.id, 30)
    elif totalInvites >= 15:
        five_invites_role = discord.utils.get(guild.roles, id=1033581373925109912)
        await user.add_roles(five_invites_role)
        await check_roles(guild, user.id, 15)
    elif totalInvites >= 5:
        five_invites_role = discord.utils.get(guild.roles, id=1033581489796939836)
        await user.add_roles(five_invites_role)
        await check_roles(guild, user.id, 5)


@client.event
async def on_message(message):
    if message.guild.id == 1039314094081183824:  # ethos
        knight = discord.utils.get(message.guild.roles, id=1045279846953132072)
        bishop = discord.utils.get(message.guild.roles, id=1045280247903424582)
        rook = discord.utils.get(message.guild.roles, id=1045279621958090872)
        queen = discord.utils.get(message.guild.roles, id=1045274556379701259)
        king = discord.utils.get(message.guild.roles, id=1045274429141299250)
        role_list = [knight, bishop, rook, queen, king]

        if check_list(role_list, message.author.roles):
            valid = True
        else:
            valid = False

    else:
        valid = True
    if valid:
        if message.guild.id == 988374126681030656 and message.channel.id == 988374129226965012:
            if message.content == "/resend-roles":
                file = discord.File("crew3_select.png", filename="crew3_select.png")
                await message.reply("Make sure to select Crew3 bot while typing the command", file=file)

        if message.guild.id == 988374126681030656:
            if 'no role' in message.content or "haven't got role" in message.content or "haven't got my role" in message.content:
                await message.reply(
                    "go to <#988374129226965012> and type /resend-roles make sure to select crew3 bot to get your roles")

        if message.guild.id == 1039314094081183824:
            if message.content.lower() == "meow" or message.content.lower()[0:9] == "mimi meow":
                await message.reply("nyaaa :cat: ")
            elif message.content.lower()[0:9] == "mimi come":
                await message.reply("NO")
            elif message.content.lower() == "i love u" or message.content.lower()[0:13] == "mimi i love u":
                await message.reply("I love u too :kissing_smiling_eyes: ")
            elif message.content.lower() == "mimi ttyl" or message.content.lower() == "mimi talk to you later":
                await message.reply("noooooooo")
            elif message.content[-1] == "?" and "mimi" in message.content.lower():
                await message.reply(random.choice(["yes", "no", "hmmmm", "meowww", "maybe", "idk", "perhaps"]))

    await client.process_commands(message)


@client.command()
async def check(ctx):
    if ctx.guild.id == 1039314094081183824:  # ethos
        knight = discord.utils.get(ctx.guild.roles, id=1045279846953132072)
        bishop = discord.utils.get(ctx.guild.roles, id=1045280247903424582)
        rook = discord.utils.get(ctx.guild.roles, id=1045279621958090872)
        queen = discord.utils.get(ctx.guild.roles, id=1045274556379701259)
        king = discord.utils.get(ctx.guild.roles, id=1045274429141299250)
        role_list = [knight, bishop, rook, queen, king]

        if check_list(role_list, ctx.author.roles):
            valid = True
        else:
            valid = False

    else:
        valid = True

    if valid:
        await ctx.send("Working :cat:")


@client.command()
async def say(ctx, *args):
    if ctx.guild.id == 1039314094081183824:  # ethos
        knight = discord.utils.get(ctx.guild.roles, id=1045279846953132072)
        bishop = discord.utils.get(ctx.guild.roles, id=1045280247903424582)
        rook = discord.utils.get(ctx.guild.roles, id=1045279621958090872)
        queen = discord.utils.get(ctx.guild.roles, id=1045274556379701259)
        king = discord.utils.get(ctx.guild.roles, id=1045274429141299250)
        role_list = [knight, bishop, rook, queen, king]

        if check_list(role_list, ctx.author.roles):
            valid = True
        else:
            valid = False
    else:
        valid = True

    if valid:
        stc = ""
        for i in args:
            stc = stc + i + " "
        await ctx.send(stc)


@client.command()
async def dance(ctx):
    if ctx.guild.id == 1039314094081183824:  # ethos
        knight = discord.utils.get(ctx.guild.roles, id=1045279846953132072)
        bishop = discord.utils.get(ctx.guild.roles, id=1045280247903424582)
        rook = discord.utils.get(ctx.guild.roles, id=1045279621958090872)
        queen = discord.utils.get(ctx.guild.roles, id=1045274556379701259)
        king = discord.utils.get(ctx.guild.roles, id=1045274429141299250)
        role_list = [knight, bishop, rook, queen, king]

        if check_list(role_list, ctx.author.roles):
            valid = True
        else:
            valid = False
    else:
        valid = True

    if valid:
        message = await ctx.send("♪┏(・o･)┛♪")
        await message.add_reaction("🎶")


@client.event
async def on_raw_reaction_add(payload):
    if str(payload.emoji) == "🎶" and not payload.member.bot:
        if payload.guild_id != 144107902587109396:
            channel = client.get_channel(payload.channel_id)
            message = await channel.fetch_message(payload.message_id)
            if message.author.id == 860904195279028245:
                await asyncio.sleep(1)
                message = await message.edit(content="♪┗ ( ･o･) ┓♪")
                await asyncio.sleep(1)
                message = await message.edit(content="♪┏(・o･)┛♪")
                await asyncio.sleep(1)
                message = await message.edit(content="♪┗ ( ･o･) ┓♪")
                await asyncio.sleep(1)
                message = await message.edit(content="♪┏(・o･)┛♪")
                await asyncio.sleep(1)
                message = await message.edit(content="♪┗ ( ･o･) ┓♪")
                await asyncio.sleep(1)
                message = await message.edit(content="♪┏(・o･)┛♪")
                user = client.get_user(payload.user_id)
                await message.remove_reaction('🎶', user)


@client.command()
async def cat(ctx):
    if ctx.guild.id == 1039314094081183824:  # ethos
        knight = discord.utils.get(ctx.guild.roles, id=1045279846953132072)
        bishop = discord.utils.get(ctx.guild.roles, id=1045280247903424582)
        rook = discord.utils.get(ctx.guild.roles, id=1045279621958090872)
        queen = discord.utils.get(ctx.guild.roles, id=1045274556379701259)
        king = discord.utils.get(ctx.guild.roles, id=1045274429141299250)
        role_list = [knight, bishop, rook, queen, king]

        if check_list(role_list, ctx.author.roles):
            valid = True
        else:
            valid = False
    else:
        valid = True

    if valid:
        headers = {
            "x-api-key": os.environ['CAT_API']
        }
        r = requests.get("https://api.thecatapi.com/v1/images/search/", headers=headers).content
        r = json.loads(r)
        await ctx.send(r[0]['url'])


@client.command()
async def selfie(ctx):
    if ctx.guild.id == 1039314094081183824:  # ethos
        knight = discord.utils.get(ctx.guild.roles, id=1045279846953132072)
        bishop = discord.utils.get(ctx.guild.roles, id=1045280247903424582)
        rook = discord.utils.get(ctx.guild.roles, id=1045279621958090872)
        queen = discord.utils.get(ctx.guild.roles, id=1045274556379701259)
        king = discord.utils.get(ctx.guild.roles, id=1045274429141299250)
        role_list = [knight, bishop, rook, queen, king]

        if check_list(role_list, ctx.author.roles):
            valid = True
        else:
            valid = False
    else:
        valid = True

    if valid:
        img_list = collection.find_one({"_id": "selfie"})['selfie_list']
        await ctx.send(random.choice(img_list))


@client.command()
async def join(ctx):
    if ctx.guild.id == 1039314094081183824:  # ethos
        knight = discord.utils.get(ctx.guild.roles, id=1045279846953132072)
        bishop = discord.utils.get(ctx.guild.roles, id=1045280247903424582)
        rook = discord.utils.get(ctx.guild.roles, id=1045279621958090872)
        queen = discord.utils.get(ctx.guild.roles, id=1045274556379701259)
        king = discord.utils.get(ctx.guild.roles, id=1045274429141299250)
        role_list = [knight, bishop, rook, queen, king]

        if check_list(role_list, ctx.author.roles):
            valid = True
        else:
            valid = False
    else:
        valid = True

    if valid:
        async for message in ctx.channel.history(limit=200):
            if message.author.id == 693167035068317736:
                if len(message.reactions) != 0:
                    await message.add_reaction(message.reactions[0])
                    await ctx.send("RUMBLE TIMEEEE")


@client.command()
async def unjoin(ctx):
    if ctx.guild.id == 1039314094081183824:  # ethos
        knight = discord.utils.get(ctx.guild.roles, id=1045279846953132072)
        bishop = discord.utils.get(ctx.guild.roles, id=1045280247903424582)
        rook = discord.utils.get(ctx.guild.roles, id=1045279621958090872)
        queen = discord.utils.get(ctx.guild.roles, id=1045274556379701259)
        king = discord.utils.get(ctx.guild.roles, id=1045274429141299250)
        role_list = [knight, bishop, rook, queen, king]

        if check_list(role_list, ctx.author.roles):
            valid = True
        else:
            valid = False
    else:
        valid = True

    if valid:
        async for message in ctx.channel.history(limit=200):
            if message.author.id == 693167035068317736:
                if len(message.reactions) != 0:
                    await message.remove_reaction(message.reactions[0], client.get_user(860904195279028245))
                    await ctx.send(":(((")
                 

@client.command()
async def add_to_selfie(ctx, link):
    try:
        if link[0:3] == '```':
            target = collection.find_one({"_id": "selfie"})['selfie_list']
            print("here")
            target.append(link[3:-3])
            collection.update_one({"_id": "selfie"}, {"$set": {"selfie_list": target}})
            await ctx.send("Added successfully!!")
        else:
            await ctx.send("Wrong formate")
    except:
        await ctx.send("Error while adding")
 

client.run(os.environ["DISCORD_TOKEN"])
