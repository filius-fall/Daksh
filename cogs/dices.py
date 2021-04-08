import random

from discord.ext import commands

class Dices(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(brief="Gives a random number between 1 and 12")
    async def roll(self,ctx):
        r = random.randrange(1,13)
        await ctx.send(r)


def setup(bot):
    bot.add_cog(Dices(bot))