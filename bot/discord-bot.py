# bot.py
import os
import random
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client(intents = discord.Intents.all())
global conversation_state
global user_in_conversation
conversation_state = ""
user_in_conversation = ""
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
    global conversation_state
    global user_in_conversation

    if message.author == client.user:
        return
    print(f'Message from {message.author}: {message.content}')

    if "<@1213544417340956732>" in message.content.lower():
        if conversation_state == "Done" or conversation_state == "":
            conversation_state == "Start"
            response = ('Hello ' + str(message.author) + '! What do you need help with?\n 🗒️ to create notecards using supplied notes \n 📝 to create notecards using a broad subject \n 🎮 to Start a kahoot quiz \n 🛑 to end our conversation')
            sent_message = await message.channel.send(response)
            user_in_conversation = message.author
            await sent_message.add_reaction('🗒️')
            await sent_message.add_reaction('📝')
            await sent_message.add_reaction('🎮')
            await sent_message.add_reaction('🛑')



@client.event
async def on_reaction_add(reaction,user):
    if reaction.me == client.user:
        return
    if str(reaction.emoji) == '🗒️':
        conversation_state =="Waiting for Notes"
        response =(f'Send your notes below to get them converted to notecards!\n ')
        sent_message = await reaction.message.channel.send(response)
        

    

    



client.run(TOKEN)