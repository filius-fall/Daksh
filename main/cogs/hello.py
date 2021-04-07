from discord.ext import commands

a = "Idiot know abot the command before typing it"
class Hello(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def hello(self,c,arg=a,*args):
        if arg == a:
            await c.send('{}'.format(a))
        else:
            await c.send('Welcome {}'.format(arg))

        for i in args:
            await c.send('Welcome {}'.format(i))


def setup(bot):
    bot.add_cog(Hello(bot))
