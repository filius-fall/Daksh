from discord.ext import commands
import random

class Coin(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(brief = "Flips a Coin to give Heads or Tails")
    async def coin(self,c):
        r = random.randrange(0,2)
        if r == 0:
            n = 'Heads'
        else:
            n = 'Tails'
        print(r)
        await c.send(n)

def setup(bot):
    bot.add_cog(Coin(bot))  
