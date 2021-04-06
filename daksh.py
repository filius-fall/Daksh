# import os
# import discord

# import dotenv as load_dotenv


# load_dotenv()
# TOKEN = os.getenv('DISCORD_TOKEN')

# client = discord.Client()

# @client.event
# async def on_ready():
#     print(f'{client.user} is connected to the discord')

# client.run(TOKEN)


# Second veriosn code
import os

# import discord
# from dotenv import load_dotenv

# load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# client = discord.Client()

# @client.event
# async def on_ready():
#     print(f'{client.user} has connected to Discord!')

# client.run(TOKEN) 

import discord

class MyClass(discord.Client):
    async def on_load(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self,message):
        print('Message recieved from {0.author}!: {0.content}'.format(message))

client = MyClass()
client.run(TOKEN)