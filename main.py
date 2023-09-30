import discord
import os
from dotenv import load_dotenv
from bot_reply import story_generator
from datetime import datetime

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)


@bot.event
async def on_ready():
    guild_count = 0

    # Count number of guilds the bot is present in
    for guild in bot.guilds:
        guild_count = guild_count + 1

    print("The bot has started! Currenlty working in " + str(guild_count) + " guild.")


@bot.event
async def on_message(message):
    msg = message.content

    if msg.startswith("<@1157375972908212294>"):
        # Clean the content before generation
        msg = msg.replace("<@1157375972908212294>", "")

        # Send a wait message
        await message.channel.send("Cooking your story.....")

        # Perform the generation and send the message
        reply = story_generator(msg) + "\nBOOM! Next time let's continue"
        await message.channel.send(reply)
        print("LOG ["+ str(datetime.now()) +"]: STATUS [200]: Message [Story generated]")

bot.run(DISCORD_TOKEN)
