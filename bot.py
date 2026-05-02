import os
import discord
from discord.ext import commands
from keep_alive import keep_alive  # Import the new function

# Your standard bot setup
bot = commands.Bot(command_prefix="!", intents=discord.Intents.default())

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

# ... (your other Hermes logic / MongoDB connections here) ...

if __name__ == "__main__":
    # 1. Start the background web server
    keep_alive()
    
    # 2. Start the Discord bot (This blocks the main thread)
    DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")
    if not DISCORD_TOKEN:
        print("Error: DISCORD_TOKEN is missing!")
    else:
        bot.run(DISCORD_TOKEN)
