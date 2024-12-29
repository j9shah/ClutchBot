import discord
from discord.ext import commands

# intents setup
intents = discord.Intents.default()
intents.message_content = True

# create bot
bot = commands.Bot(command_prefix="!", intents=intents)

# event: bot is ready
@bot.event
async def on_ready():
    print(f"{bot.user} is now running!")
    print("Bot is ready and listening for commands...")

# command: ping
@bot.command()
async def ping(ctx):
    print(f"Ping command received in channel: {ctx.channel}")
    await ctx.send("Pong!")

# run bot
bot.run("REMOVED")