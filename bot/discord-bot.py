# bot.py
import os
import random
import discord
import asyncio
import json
import time
from dotenv import load_dotenv
from aifunc import ParseJSON, gptCall, custom_notes

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client(intents = discord.Intents.all())
global subject
global txtFileRead
global customNotes
subject = ""
txtFileRead = ""
customNotes = False

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
    global subject
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
            if txtFileRead == 'flashcards':
                try:
                    # Read the content of the text file
                    file_content = await file.read()

                    # Process the file content as a string
                    subject = file_content.decode('utf-8')
                    
                    # Print or log the string content for inspection
                    print("File Content:", subject)

                    await message.channel.send("Got it! Looks good to me!")
                    response = ('How many notecards would you like to be made?\n 5️⃣ for 5 \n 1️⃣ for 10 \n 2️⃣ for 20 \n 3️⃣ for 30')
                    sent_message = await message.channel.send(response)
                    await sent_message.add_reaction('5️⃣')
                    await sent_message.add_reaction('1️⃣')
                    await sent_message.add_reaction('2️⃣')
                    await sent_message.add_reaction('3️⃣')
                except discord.HTTPException as e:
                    await message.channel.send(f"Error reading the file: {e}")
            elif txtFileRead == "kahoot":
                try:
                    # Read the content of the text file
                    file_content = await file.read()

                    # Process the file content as a string
                    subject = file_content.decode('utf-8')
                    
                    # Print or log the string content for inspection
                    print("File Content:", subject)

                    await message.channel.send("Got it! Looks good to me!")
                    response = ('How many questions would you like to be made?\n\n🅰️ for 10 \n🅱️ for 20')
                    sent_message = await message.channel.send(response)
                    await sent_message.add_reaction('🅰️')
                    await sent_message.add_reaction('🅱️')
                except discord.HTTPException as e:
                    await message.channel.send(f"Error reading the file: {e}")
        else:
            await message.channel.send("Please attach a text file.")


#TODO: turn this into a switch statement
@client.event
async def on_reaction_add(reaction,user):
    global subject
    global txtFileRead
    global customNotes
    customNotes = False
    notecard_list = []
    question_list = []
    if user == client.user:
        return
    if str(reaction.emoji) == '🗒️':
        response =(f'What subject do you want to cover in the notecards?')
        await reaction.message.channel.send(response)
        response_message = await client.wait_for('message', check=lambda m: m.author == user and m.channel == reaction.message.channel, timeout=60)
        user_topic = response_message.content
        response =(f'Send your notes below to get them converted to notecards!\n ')
        customNotes = True
        txtFileRead = 'flashcards'
        sent_message = await reaction.message.channel.send(response)
    elif str(reaction.emoji) == '📝':
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
        await reaction.message.channel.send("Creating 5 notecards please be patient...")
        print(f'Subject Value: {subject}')
        print(f'customNotes Value: {customNotes}')
        if customNotes:
            notecard_list = ParseJSON.formatFlashcard((custom_notes.gptCallFlashcards(subject, user_topic, "5")))
        else:
            notecard_list = ParseJSON.formatFlashcard(gptCall.gptCallFlashcards("5",subject))
        for notecard in notecard_list:
            await reaction.message.channel.send(notecard)
            time.sleep(0.5)
        await reaction.message.channel.send("All done! Please ping me again if you'd need a Study Buddy!")
    elif str(reaction.emoji) == '1️⃣':
        await reaction.message.channel.send("Creating 10 notecards please be patient...")
        if customNotes:
            notecard_list = ParseJSON.formatFlashcard((custom_notes.gptCallFlashcards(subject, user_topic, "10")))
        else:
            notecard_list = ParseJSON.formatFlashcard(gptCall.gptCallFlashcards("10",subject))
        for notecard in notecard_list:
            await reaction.message.channel.send(notecard)
            time.sleep(0.5)
        await reaction.message.channel.send("All done! Please ping me again if you'd need a Study Buddy!")
    elif str(reaction.emoji) == '2️⃣':
        await reaction.message.channel.send("Creating 20 notecards please be patient...")
        if customNotes:
            notecard_list = ParseJSON.formatFlashcard((custom_notes.gptCallFlashcards(subject, user_topic, "5")))
        else:
            notecard_list = ParseJSON.formatFlashcard(gptCall.gptCallFlashcards("20",subject))
        for notecard in notecard_list:
            await reaction.message.channel.send(notecard)
            time.sleep(0.5)
        await reaction.message.channel.send("All done! Please ping me again if you'd need a Study Buddy!")
    elif str(reaction.emoji) == '3️⃣':
        await reaction.message.channel.send("Creating 30 notecards please be patient...")
        if customNotes:
            notecard_list = ParseJSON.formatFlashcard((custom_notes.gptCallFlashcards(subject, user_topic, "5")))
        else:
            notecard_list = ParseJSON.formatFlashcard(gptCall.gptCallFlashcards("30",subject))
        for notecard in notecard_list:
            await reaction.message.channel.send(notecard)
            time.sleep(0.5)
        await reaction.message.channel.send("All done! Please ping me again if you'd need a Study Buddy!")
    elif str(reaction.emoji) == "🎮":
        await start_game(reaction.message)
    elif str(reaction.emoji) =="🛑":
        await reaction.message.channel.send("Okay Im always available if you ever need me!")
        return
    if str(reaction.emoji) == '📃':
        response =(f'Send your notes below to get them converted to questions!\n')
        txtFileRead = 'kahoot'
        sent_message = await reaction.message.channel.send(response)
    elif str(reaction.emoji) == '⌨️':
        response = ('How many questions would you like to be made?\n\n🅰️ for 10 \n🅱️ for 20')
        sent_message = await reaction.message.channel.send(response)
        await sent_message.add_reaction('🅰️')
        await sent_message.add_reaction('🅱️')
    if str(reaction.emoji) == '🅰️':
        await reaction.message.channel.send("Great! Now just send a message with the overall topic you'd like to review")
        response_message = await client.wait_for('message', check=lambda m: m.author == user and m.channel == reaction.message.channel, timeout=60)
        user_topic = response_message.content
        await reaction.message.channel.send("Creating 10 questions please be patient...")
        if customNotes:
            question_list = ParseJSON.formatKahoot(custom_notes.notesGptCallKahoot(subject, user_topic, "10"))
        else:
            question_list = ParseJSON.formatKahoot(gptCall.gptCallKahoot("10", user_topic))
        for question in ((question_list)):
            asked_question = await reaction.message.channel.send(question)
            await asked_question.add_reaction('🟥')
            await asked_question.add_reaction('🟨')
            await asked_question.add_reaction('🟩')
            await asked_question.add_reaction('🟦')
            time.sleep(5)
    elif str(reaction.emoji) == '🅱️':
        await reaction.message.channel.send("Great! Now just send a message with the overall topic you'd like to review")
        response_message = await client.wait_for('message', check=lambda m: m.author == user and m.channel == reaction.message.channel, timeout=60)
        user_topic = response_message.content
        await reaction.message.channel.send("Creating 20 questions please be patient...")
        if customNotes:
            question_list = ParseJSON.formatKahoot(custom_notes.notesGptCallKahoot(subject, user_topic, "20"))
        else:
            question_list = ParseJSON.formatKahoot(gptCall.gptCallKahoot("20", user_topic))
        for question in question_list:
            await reaction.message.channel.send(question)
            time.sleep(0.5)
    if str(reaction.emoji) in '🟥🟨🟩🟦':
        pass


#TODO: get players, prompt user for a file input or a prompt input, generate questions, create embed with reactions, 
#keep score, print winner
async def start_game(message):
    # Send a message to prompt players to join
    join_message = await message.channel.send(" @everyone React with ✅ to join the review!")
    await join_message.add_reaction('✅')

    # Wait for players to join
    def check(reaction, user):
        return str(reaction.emoji) == '✅' and reaction.message == join_message and user != client.user
    

    async def get_user_prompt(message):
        intro_message = ('Welcome to StudyBuddy\'s Quick Questions, where your speed and knowledge are put to the test.\nThe rules are quite simple: Be fast and pick the correct answer by reacting with the correct color.\n Good luck!')
        user_prompt = ('Now, what topic would you like to cover today?\nReact with a 📃 to enter a .txt file\nReact with a ⌨️ to give StudyBuddy a prompt')
        await message.channel.send(intro_message)
        sent_user_prompt = await message.channel.send(user_prompt)
        await sent_user_prompt.add_reaction('📃')
        await sent_user_prompt.add_reaction('⌨️')

    def update_scoreboard():
        pass

    players = []
    while True:
        try:
            reaction, user = await client.wait_for('reaction_add', timeout=10.0, check=check)
            players.append(user)
        except asyncio.TimeoutError:
            break
    
    if len(players) < 1: #TODO: CHANGE BACK TO 2
        await message.channel.send("Not enough players to start the game.")
        return
    player_names = ', '.join([player.name for player in players])
    await message.channel.send(f"Players in the game: {player_names}")
    await get_user_prompt(message)




    

    



client.run(TOKEN)