import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json

with open('setting.json',mode='r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

class React(Cog_Extension):

    @commands.command()
    async def 呵(self, ctx):
        pic = discord.File(jdata['pic'])
        await ctx.send(file = pic)

    @commands.command()
    async def tmd(self, ctx):
        pic = discord.File(jdata['pic2'])
        await ctx.send(file = pic)


    

def setup(bot):
    bot.add_cog(React(bot))
