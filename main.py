from discord.ext import commands
import os
import discord
# from dotenv import load_dotenv

from settings import *

# load_dotenv()
# TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix="!")

# @bot.event
# async def on_ready():
#     print(f'{bot.user.name} is logged')

class Hello(discord.Client):
    
    async def on_message(self,ctx):
        print(f'{self.user} is ligged')




# bot.load_extension(f'cogs.test')
# bot.load_extension(f'cogs.hello')
# bot.load_extension(f'cogs.fake_test')

for filename in os.listdir("./cogs"):
    if filename.endswith(".py") and filename != "__init__.py":
        bot.load_extension(f'cogs.{filename[:-3]}')

# bot.run(TOKEN)
# print('HELLI')
# print(DISCORD_TOKEN)

bot.run(DISCORD_TOKEN)
# c = Hello()
# c.run(DISCORD_TOKEN)
 