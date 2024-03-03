# bot.py
import os
import random
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client(intents = discord.Intents.all())

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

        response = (f'Hello ' + str(message.author) + '! What do you need help with?\n 🗒️ to create notecards using supplied notes \n 📝 to create notecards using a broad subject \n 🎮 to Start a kahoot quiz')
        personTalking = message.author
        sent_message = await message.channel.send(response)
        await sent_message.add_reaction('🗒️')
        await sent_message.add_reaction('🎮')
async def on_reaction_add(reaction,user):
    if reaction.message.content.startswith("Hello") and str(reaction.emoji) == "🗒️":
        response =(f'Send your notes below to get them converted to notecards!\n ')
        send_message = await message.channel.send(response)
        await reaction.message.channel.send('What topic would you like to have notecards for?')
        

    



client.run(TOKEN)