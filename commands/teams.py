import discord
from discord.ext import commands
from utils.api_handler import fetch_teams

class Teams(commands.Cog):
    """Teams command."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="teams", aliases=["teamlist"])
    async def teams(self, ctx):
        """List all NBA teams."""
        teams_data = fetch_teams()

        if not teams_data or not teams_data["data"]:
            await ctx.send("Failed to fetch teams data. Try again later.")
            return

        # builds list of all teams
        message = "**NBA Teams:**\n"
        for team in teams_data["data"]:
            message += f"- {team['full_name']} ({team['abbreviation']})\n"

        await ctx.send(message)

    @commands.command(name="team", aliases=["teaminfo"])
    async def team(self, ctx, *, name):
        """Fetch information about a specific NBA team."""
        teams_data = fetch_teams()

        if not teams_data or not teams_data["data"]:
            await ctx.send("Failed to fetch team data. Try again later.")
            return

        # allows partial matching for team names
        team = next((t for t in teams_data["data"] if name.lower() in t["full_name"].lower()), None)
        if not team:
            await ctx.send(f"Team '{name}' not found. Try using the full or partial team name.")
            return

        message = (
            f"**{team['full_name']}**\n"
            f"Abbreviation: {team['abbreviation']}\n"
            f"City: {team['city']}\n"
            f"Conference: {team['conference']}\n"
            f"Division: {team['division']}"
        )
        await ctx.send(message)

async def setup(bot):
    """Asynchronously add the cog to the bot."""
    await bot.add_cog(Teams(bot))