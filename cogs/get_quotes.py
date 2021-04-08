from discord.ext import commands
from settings import *
import os
import json
import random


class Quotes(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def quotes(self,ctx):
        with open(os.path.join(DATA_DIR,'quotes.json')) as quotes_file:
            quote = json.load(quotes_file)
        random_quote = random.choice(list(quote.keys()))
        r = random.choice(quote[random_quote])
        
        await ctx.send(r['quote'])
        # print(r['quote'])

        


def setup(bot):
    bot.add_cog(Quotes(bot))