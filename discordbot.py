import discord 
from discord.ext import commands

import settings

token = settings.TOKEN
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!?', intents=intents)

cogs = [

    'cogs.main',
]

for cog in cogs:
    bot.load_extension(cog)

bot.run(token)