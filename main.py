import discord
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))


    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

        COMMAND_PREFIX = "!"

        if message.content[0] != COMMAND_PREFIX:
            return

        split_msg = message.content.split(" ")
        cmd = split_msg[0]
        if len(split_msg) > 1:
            args = split_msg[1]

        if cmd == "!name":
            print(message.author.name)
            print('hhhh')
            await message.channel.send("!name")

client = MyClient()
client.run(TOKEN)