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
                subject = f"File Content:\n```{file_content.decode('utf-8')}```"
                await message.channel.send(subject)
            except discord.HTTPException as e:
                await message.channel.send(f"Error reading the file: {e}")
        else:
            await message.channel.send("Please attach a text (.txt) file.")



@client.event
async def on_reaction_add(reaction,user):
    if user == client.user:
        return
    if str(reaction.emoji) == '🗒️' and reaction.me != client.user:
        response =(f'Send your notes below in a .txt file to get them converted to notecards!')
        sent_message = await reaction.message.channel.send(response)
        

    

    



client.run(TOKEN)