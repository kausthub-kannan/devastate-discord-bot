from dotenv import load_dotenv
import os
from datetime import datetime
import discord
from discord.ext import commands
from discord import app_commands
from bot_reply import story_generator, get_meme


# Load the Bot Token
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")


# Specify the permissions
intents = discord.Intents.default()
intents.message_content = True


# Create the bot
bot = commands.Bot(command_prefix="!", intents=intents)


# Sync commands
@bot.event
async def on_ready():
    guild_count = 0

    # Count number of guilds the bot is present in
    for guild in bot.guilds:
        guild_count = guild_count + 1

    try:
        synced = await bot.tree.sync()
        print("Commands synced")
    except Exception as e:
        print(e)

    print("The bot has started! Currenlty working in " + str(guild_count) + " guild.")


# Story Generation
@bot.tree.command(name="story", description="story generation")
@app_commands.describe(text = "The story of")
async def send_story(interaction: discord.Interaction, text: str):

    # Perform the generation and send the message
    reply = story_generator(text)
    
    # LOG
    log = "LOG ["+ str(datetime.now()) +"]: STATUS [200]: Message [Story generated]"
    print(log)

    await interaction.response.send_message(reply)


# Meme Generation Command
@bot.tree.command(name="meme", description="random meme")
async def send_meme(interaction: discord.Interaction):

    # Get meme data from API
    data = await get_meme()
    meme = data["meme"]

    # LOG
    log = "LOG ["+ str(datetime.now()) +"]: STATUS [200]: Message [Meme generated]"
    print(log)

    # Reply to the user and send the meme
    await interaction.response.send_message(meme["image url"])

bot.run(DISCORD_TOKEN)
