import discord
from brain import response_setence, bot_name
from config import mytoken_discord
import asyncio

#TODO make a wellcome to new members

# This variable says whether the bot should respond to chat messages or not
should_response = False
bot_name = bot_name
bot_nickname = 'prime'

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    # When the variable 'should_response' change to True, this func is activate
    async def reset_should_respond(self): # Then in 10min the variable is changed to False again
        global should_respond
        await asyncio.sleep(10 * 60)  # Wait 10min
        print('TIME OUT: call again bot with "luana" or "lu"')
        should_respond = False

    async def on_message(self, msg):
        channel = msg.channel
        if msg.author == self.user:
            return
        
        if bot_name in msg.content.lower() or bot_nickname in msg.content.lower():
            should_respond = True
            await msg.reply(response_setence(msg.content), mention_author=True)

            await self.reset_should_respond()

        if should_respond:
            if 'stop' in msg.content:
                should_respond = False
            await channel.send(response_setence(msg.content))


intents = discord.Intents.all()
intents.message_content = True
client = MyClient(intents=intents)
client.run(mytoken_discord)
