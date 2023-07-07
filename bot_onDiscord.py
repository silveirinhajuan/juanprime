import discord
from brain import response_setence

from config import mytoken_discord

should_response = False


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def reset_should_respond(self):
        global should_respond
        await asyncio.sleep(10 * 60)  # espera 10 minutos
        print('TIME OUT: call again bot with "luana" or "lu"')
        should_respond = False

    async def on_message(self, msg):
        channel = msg.channel
        if msg.author == self.user:
            return

        await channel.send(response_setence(msg.content))


intents = discord.Intents.all()
intents.message_content = True
client = MyClient(intents=intents)
client.run(mytoken_discord)
