# bot.py
import os
import random
import discord
import logging
from dotenv import load_dotenv

#TODO: set up logging if needed with: discord.utils.setup_logging()

#GET TOKEN AND SERVER NAME FROM ENV
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
client = discord.Client(intents = discord.Intents.all())


#CLIENT EVENTS
@client.event
async def on_ready():
    guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)
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


    corey_titles = [
        'That\'s Lord Emperor to you!',
        'May his Lordship be blessed eternally',
        'Praise be to the Lord Emperor'
    ]
    
    if "corey" in message.content.lower():
        response = random.choice(corey_titles)
        await message.channel.send(response)
    



client.run(TOKEN)