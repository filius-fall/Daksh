import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
VALUE = os.getenv('DEFAULT_MESSAGE')

bot = commands.Bot(command_prefix='!')

@commands.command()
async def p(c):                                 # name of the function should be the command like !p is the command you are writing function for
    await c.send("HEY")                         # the argument can be anything you used c others can also be used


@commands.command()
async def hello(d,arg=VALUE,*args):
    
    await d.send("Hello {}".format(arg))

    for i in args:
        await d.send("Hello {}".format(i))


bot.add_command(p)
bot.add_command(hello)

bot.run(TOKEN)

