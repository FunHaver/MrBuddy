from discord.ext.commands import Bot
import asyncio
import aiohttp
import json
import random
import subprocess

BOT_TOKEN = ''

client = Bot(command_prefix='!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if 'Hey MrBuddy' in message.content:
        trimmed_message = message.content[12:]
        escaped_message = ""
        for i in range(0, len(trimmed_message)):
            if trimmed_message[i] == " ":
                trimmed_message += ""
            escaped_message += trimmed_message[i]
        print(escaped_message)
        
        subprocess.run(["/home/conor/DiscordBot/execute-gpt2.sh", escaped_message])
        generated_text = open("output.txt", "r")
        await message.channel.send(generated_text.read())

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(BOT_TOKEN)
