import discord
from discord.ext import commands

class Help(commands.Cog):
    """Help command for the bot."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="bothelp", aliases=["commands", "assist"])
    async def bothelp(self, ctx):
        """
        Display a list of all available bot commands.
        """
        help_message = (
            "**ClutchBot Commands:**\n"
            "1. `!scores` or `!games`: Fetch scores of recent games.\n"
            "2. `!teams`: List all NBA teams.\n"
            "3. `!player <name>`: Fetch player details.\n"
            "4. `!predict <team1> <team2>`: Predict the outcome of a game between two teams.\n"
            "5. `!bothelp` or `!commands`: Display this help message."
        )
        await ctx.send(help_message)

async def setup(bot):
    await bot.add_cog(Help(bot))