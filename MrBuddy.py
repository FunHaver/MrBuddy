from discord.ext.commands import Bot
import asyncio
import aiohttp
import subprocess

BOT_TOKEN = ''

client = Bot(command_prefix='!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if 'Hey MrBuddy' in message.content:
        trimmed_message = message.content[12:]
        print(trimmed_message)
        
        subprocess.run(["/home/conor/DiscordBot/execute-gpt2.sh", trimmed_message])
        generated_text = open("output.txt", "r")
        await message.channel.send(generated_text.read())

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(BOT_TOKEN)
