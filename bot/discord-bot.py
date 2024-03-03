# bot.py
import os
import random
import discord
from dotenv import load_dotenv
from aifunc import ParseJSON, gptCall, custom_notes

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
        await sent_message.add_reaction('🗒️')
        await sent_message.add_reaction('📝')
        await sent_message.add_reaction('🎮')
        await sent_message.add_reaction('🛑')
    # Check if the message has attachments
    if message.attachments:
        # Assuming only one file is attached; you can modify accordingly
        file = message.attachments[0]

        # Check if the file is a text file (you can customize this check)
        if file.filename.endswith('.txt'):
            try:
                # Read the content of the text file
                file_content = await file.read()

                # Process the file content (you can customize this part)
                # In this example, let's just send the content back to the channel
                subject = f"{file_content.decode('utf-8')}"
                await message.channel.send("Got it! Looks good to me!")
                response = ('How many notecards would you like to be made?\n 5️⃣ for 5 \n 1️⃣ for 10 \n 2️⃣ for 20 \n 3️⃣ for 30')
                sent_message = await message.channel.send(response)
                await sent_message.add_reaction('5️⃣')
                await sent_message.add_reaction('1️⃣')
                await sent_message.add_reaction('2️⃣')
                await sent_message.add_reaction('3️⃣')
            except discord.HTTPException as e:
                await message.channel.send(f"Error reading the file: {e}")
        else:
            await message.channel.send("Please attach a text (.txt) file.")



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
        await reaction.message.channel.send("Creating  5 notecards please be patient...")
        await reaction.message.channel.send((gptCall.gptCallFlashcards("5",subject)))
        await reaction.message.channel.send(ParseJSON.formatFlashcard(gptCall.gptCallFlashcards("5",subject)))
    elif str(reaction.emoji) == '1️⃣':
        await reaction.message.channel.send("Creating 10 notecards please be patient...")
        await reaction.message.channel.send(ParseJSON.formatFlashcard(gptCall.gptCallFlashcards("10",subject)))
    elif str(reaction.emoji) == '2️⃣':
        await reaction.message.channel.send("Creating 20 notecards please be patient...")
        await reaction.message.channel.send(ParseJSON.formatFlashcard(gptCall.gptCallFlashcards("20",subject)))
    elif str(reaction.emoji) == '3️⃣':
        await reaction.message.channel.send("Creating 30 notecards please be patient...")
        await reaction.message.channel.send(ParseJSON.formatFlashcard(gptCall.gptCallFlashcards("30",subject)))
#  elif str(reaction.emoji) == "🎮"
    elif str(reaction.emoji) =="🛑":
        await reaction.message.channel.send("Okay Im always available if you ever need me!")
        return 


    

    



client.run(TOKEN)