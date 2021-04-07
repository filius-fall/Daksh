from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix="!")


bot.load_extension(f'cogs.test')
bot.load_extension(f'cogs.hello')
bot.load_extension(f'cogs.fake_test')

bot.run(TOKEN)

