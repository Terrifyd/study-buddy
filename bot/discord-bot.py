# bot.py
import os
import random
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

# intents = discord.Intents.default()
# intents.message_content = True
# client = discord.Client(intents=intents)

client = discord.Client(intents = discord.Intents.default())

@client.event
async def on_ready():
    guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    print(discord.Intents.message_content in discord.Intents.default())

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, glad you could join the study session!'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        print("no recursion")
        return

    corey_titles = [
        'That\'s Lord Emperor to you!',
        'May his Lordship be blessed eternally',
        'Praise be to the Lord Emperor'
    ]

    if "corey" in message.content.lower():
        print("in the corey if")
        response = random.choice(corey_titles)
        print("random choice")
        await message.channel.send(response)



client.run(TOKEN)