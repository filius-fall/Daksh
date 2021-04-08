from discord.ext import commands

class SelfDestruct(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(brief = "Self-Destruct on given time in mentioned or else default to 10")
    async def self_destruct(self,c,arg=10):
        await c.send('Initiating Self-Destruct sequence')
        i = arg
        while arg > 0:
            await c.send('Self Destrucuting in {} secs'.format(arg))
            if arg == 1:
                await c.send('KABOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOM')
                await c.send('YOU ARE DEAD')
                return
            arg = arg - 1
def setup(bot):
    bot.add_cog(SelfDestruct(bot))