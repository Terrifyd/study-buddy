# bot.py
import os
import random
from discord.ext import commands
import discord
import logging
from discord.ext import commands
from dotenv import load_dotenv

#TODO: set up logging if needed with: discord.utils.setup_logging()

#GET TOKEN AND SERVER NAME FROM ENV
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
intents = discord.Intents.all()
client = discord.Client(intents = intents)
bot = commands.Bot(command_prefix='?', intents=intents)

#CLIENT EVENTS
@client.event
async def on_ready():
    guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)
    await client.change_presence(activity=discord.Game('@ me for a Study Buddy!'))
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, glad you could join the study session!'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    print(f'Message from {message.author}: {message.content}')    

    if "<@1213544417340956732>" in message.content.lower():
        response = random.choice(corey_titles)
        await message.channel.send (corey_titles)
    



#client.run(TOKEN)
bot.run(TOKEN)