import discord
from discord.ext import commands
from datetime import datetime
from utils.api_handler import fetch_scores

class Scores(commands.Cog):
    """Scores command."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def scores(self, ctx):
        """Fetch today's NBA scores."""
        today = datetime.now().strftime('%Y-%m-%d')
        games_data = fetch_scores(today)

        if not games_data or not games_data["data"]:
            await ctx.send("No NBA games are live today.")
            return

        message = "**Today's NBA Games:**\n"
        for game in games_data["data"]:
            message += (f"{game['home_team']['full_name']} ({game['home_team_score']}) vs "
                        f"{game['visitor_team']['full_name']} ({game['visitor_team_score']}) - {game['status']}\n")
        await ctx.send(message)

async def setup(bot):
    """Asynchronously add the cog to the bot."""
    await bot.add_cog(Scores(bot))