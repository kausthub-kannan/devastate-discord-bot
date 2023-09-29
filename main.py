import discord
import os
from dotenv import load_dotenv
from discord.ext import commands  # necessary for this task
from code_helper import code_helper

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
intents = discord.Intents.default()
intents.message_content = True

bot = discord.Client(intents=intents)


@bot.event
async def on_ready():
    guild_count = 0
    for guild in bot.guilds:
        # PRINT THE SERVER'S ID AND NAME.
        print(f"- {guild.id} (name: {guild.name})")

        # INCREMENTS THE GUILD COUNTER.
        guild_count = guild_count + 1

    # PRINTS HOW MANY GUILDS / SERVERS THE BOT IS IN.
    print("Devastate is in " + str(guild_count) + " guild.")


@bot.event
async def on_message(message):
    print(message.content)
    msg = message.content
    # CHECKS IF THE MESSAGE THAT WAS SENT IS EQUAL TO "HELLO".
    if msg.startswith("<@1157375972908212294>"):
        # SENDS BACK A MESSAGE TO THE CHANNEL.
        msg = msg.lower()
        reply = code_helper(msg)
        await message.channel.send(reply)

    # EXECUTES THE BOT WITH THE SPECIFIED TOKEN. TOKEN HAS BEEN REMOVED AND USED JUST AS AN EXAMPLE.


bot.run(DISCORD_TOKEN)
