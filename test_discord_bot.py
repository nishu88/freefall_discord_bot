import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import os

Client = discord.Client()
client = commands.Bot(command_prefix = "?")

chat_filter = ["PINEAPPLE", "APPLE", "CHROME"]
bypass_list = []
print("HI there")
@client.event
async def on_ready():
    print("Bot is online and connected to Discord")
    await client.change_presence(game=discord.Game(name="Busy Being AWESOME"))

##@client.event
##async def on_message(message):
##    if message.content == "cookie":
##        await client.send_message(message.channel, ":cookie:") #responds with Cookie emoji when someone says "cookie"

@client.event
async def on_message(message):
    if message.content.upper().startswith('!PING'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Pong!" % (userID))
    if message.content.upper().startswith('!SAY'):
        args = message.content.split(" ")
        #args[0] = !SAY
        #args[1] = Hey
        #args[2] = There
        #args[1:] = Hey There
        await client.send_message(message.channel, "%s" % (" ".join(args[1:])))

##@client.event
##async def on_message(message):
##    contents = message.content.split(" ") #contents is a list type
##    for word in contents:
##        if word.upper() in chat_filter:
##            if not message.author.id in bypass_list:
##                try:
##                    await client.delete_message(message)
##                    await client.send_message(message.channel, "**Hey!** You're not allowed to use that word here!")
##                except discord.errors.NotFound:
##                    return
                    
        

client.run(os.getenv('TOKEN'))
