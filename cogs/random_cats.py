from discord.ext import commands
import aiohttp
import os
import discord
import json


class Cats(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def cats(self,ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("http://aws.random.cat/meow") as r:

                data = await r.json()
                embeded = discord.Embed(title="Meow")
                embeded.set_image(url=data['file'])
                embeded.set_footer(text='http://aws.random.cat') 
                print('RANDOMS CAT IMAGE IS GENERATED')

                await ctx.send(embed=embeded)   

def setup(bot):
    bot.add_cog(Cats(bot))