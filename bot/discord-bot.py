# bot.py
import os
import random
import discord
from dotenv import load_dotenv
from aifunc import gptCall, custom_notes

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client(intents = discord.Intents.all())
global subject
subject = ""
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
        response = ('Hello ' + str(message.author) + '! What do you need help with?\n 🗒️ to create notecards using supplied notes \n 📝 to create notecards using a broad subject \n 🎮 to Start a kahoot quiz \n 🛑 to end our conversation')
        sent_message = await message.channel.send(response)
        user_in_conversation = message.author
        await sent_message.add_reaction('🗒️')
        await sent_message.add_reaction('📝')
        await sent_message.add_reaction('🎮')
        await sent_message.add_reaction('🛑')



@client.event
async def on_reaction_add(reaction,user):
    global subject
    if user == client.user:
        return
    if str(reaction.emoji) == '🗒️':
        response =(f'Send your notes below to get them converted to notecards!\n ')
        sent_message = await reaction.message.channel.send(response)
    elif str(reaction.emoji) == "📝":
        response =(f'What subject do you want to cover in the notecards?')
        await reaction.message.channel.send(response)
        response_message = await client.wait_for('message', check=lambda m: m.author == user and m.channel == reaction.message.channel, timeout=60)
        subject = response_message.content
        response = ('How many notecards would you like to be made?\n 5️⃣ for 5 \n 1️⃣ for 10 \n 2️⃣ for 20 \n 3️⃣ for 30')
        sent_message = await reaction.message.channel.send(response)
        await sent_message.add_reaction('5️⃣')
        await sent_message.add_reaction('1️⃣')
        await sent_message.add_reaction('2️⃣')
        await sent_message.add_reaction('3️⃣')
    if str(reaction.emoji) == '5️⃣':
        await reaction.message.channel.send("Creating notecards please be patient...")
        await reaction.message.channel.send(gptCall.gptCallFlashcards("5",subject))
    elif str(reaction.emoji) == '1️⃣':
        await reaction.message.channel.send(gptCall.gptCallFlashcards("10",subject))
    elif str(reaction.emoji) == '2️⃣':
        await reaction.message.channel.send(gptCall.gptCallFlashcards("20",subject))
    elif str(reaction.emoji) == '3️⃣':
        await reaction.message.channel.send(gptCall.gptCallFlashcards("30",subject))
#  elif str(reaction.emoji) == "🎮"


    

    



client.run(TOKEN)