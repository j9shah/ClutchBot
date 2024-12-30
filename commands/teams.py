import discord
from discord.ext import commands
from utils.api_handler import fetch_teams

class Teams(commands.Cog):
    """Teams command."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def team(self, ctx, *, name):
        """Fetch information about an NBA team."""
        teams_data = fetch_teams()

        if not teams_data or not teams_data["data"]:
            await ctx.send("Failed to fetch team data. Try again later.")
            return

        team = next((t for t in teams_data["data"] if t["full_name"].lower() == name.lower()), None)
        if not team:
            await ctx.send(f"Team '{name}' not found.")
            return

        message = (f"**{team['full_name']}**\n"
                   f"Abbreviation: {team['abbreviation']}\n"
                   f"City: {team['city']}\n"
                   f"Conference: {team['conference']}\n"
                   f"Division: {team['division']}")
        await ctx.send(message)

async def setup(bot):
    """Asynchronously add the cog to the bot."""
    await bot.add_cog(Teams(bot))