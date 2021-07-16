from discord import channel, client, message
from discord.ext import commands
import discord
import asyncio
import random

from discord.ext.commands import context

class Main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def flash(self, ctx):
        total = 0

        for i in range(5):
            number = random.randint(10,99)
            total += number
            msg = await ctx.send(number)
            await asyncio.sleep(0.8)
            await msg.delete()
            await asyncio.sleep(0.8)

        print(total)    

        def check(msg):
            if msg.channel != ctx.channel:
                return
            if msg.content != str(total):
                return
            return True

        msg = await self.bot.wait_for('message', check=check)
        await msg.add_reaction('🎉')
 
     #応答1
    @commands.Cog.listener()
    async def on_ready(self):
        print("on_ready")
        print(discord.__version__)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        if message.content == "はふぅ":
            await message.channel.send("はふぅ!")
        if message.content == "ﾅｰﾝﾃﾞﾅﾝ":
            await message.channel.send("こっさめーん")  
        if message.content == "ぼっち":
            await message.channel.send("あまぼっち！")
        if message.content == "お願い":
            await message.channel.send("ダーリン♡")
        

def setup(bot):
    bot.add_cog(Main(bot))

  
   