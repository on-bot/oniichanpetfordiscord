from discord.ext import commands
import asyncio
from datetime import datetime
import pytz # $ pip install pytz
import requests



class Study(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.command()
    async def log(self, ctx, *, texts):
        try:
            now = datetime.now(pytz.timezone('Asia/Kathmandu'))
            strnow = str(now)
            texts_list = texts.split(' ')
            t_l = []
            for text in texts_list:
                text.capitalize()
                t_l.append(text.capitalize())

            with open('test.txt', 'r') as f:
                logs = f.read()
            with open('test.txt', 'w') as f:
                f.write(str(logs + "\n"))
                texts1 = t_l[1].split(',')
                texts1instring = ''
                for letter in texts1:
                    texts1instring = texts1instring + str(letter.capitalize()) + ' '
                f.write(strnow[:-13] + ' ' + str(t_l[0]) + ' ' + texts1instring)

            await ctx.send("Successfull")

        except:
            now = datetime.now(pytz.timezone('Asia/Kathmandu'))
            strnow = str(now)
            with open('test.txt', 'r') as f:
                logs = f.read()
            with open('test.txt', 'w') as f:
                f.write(str(logs + "\n"))
                f.write(strnow[:-13] + ' ' + texts.capitalize())
            await ctx.send("Successful But dont use This")


    @commands.command()
    async def uploadlogs(self,ctx):
        req = requests.session()
        files = {'file': open("test.txt", 'rb')}
        response = req.post('https://file.io/', files=files)
        await ctx.send(f'Uploaded {response.text}')


    @commands.command()
    async def readlogs(self, ctx):
        with open('test.txt', 'r') as f:
            logs = f.read()
        await ctx.send(logs)


def setup(client):
    client.add_cog(Study(client))
