from discord.ext import commands

class Test(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command()
    async def test(self,c):                                             #name of function is the command
        await c.send('Hello')

def setup(bot):
    bot.add_cog(Test(bot))
