import discord
from discord.ext import commands
import os
from dotenv import load_dotenv 

# load environment variables from .env
load_dotenv()

# get the bot token from the environment
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

# define intents (required for bot)
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

# initialize bot
bot = commands.Bot(command_prefix="!", intents=intents)

# load cogs (commands)
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    for filename in os.listdir('./commands'):
        if filename.endswith('.py'):
            try:
                await bot.load_extension(f'commands.{filename[:-3]}')
                print(f"Loaded extension: {filename}")
            except Exception as e:
                print(f"Failed to load extension {filename}: {e}")

# run bot
bot.run(TOKEN)