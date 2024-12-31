import discord
from discord.ext import commands
from utils.api_handler import fetch_player

class Players(commands.Cog):
    """Player command."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def player(self, ctx, *, name):
        """
        Fetch information about an NBA player by name or ID.
        If multiple names are given, use the last name for the search.
        """
        if name.isdigit():  # if the input is numeric, treat it as ID
            player_data = fetch_player(name)
            if not player_data:  # API returned no player
                await ctx.send(f"No player found with ID '{name}'. Please try another ID.")
                return

            # handle player object (ID search)
            player = player_data
            height = player.get("height", "Height not available")
            weight = player.get("weight", "N/A lbs")
            team = player["team"]["full_name"] if player.get("team") else "Free Agent"
            message = (
                f"**{player['first_name']} {player['last_name']}**\n"
                f"Position: {player.get('position', 'N/A')}\n"
                f"Team: {team}\n"
                f"Height: {height}\n"
                f"Weight: {weight}"
            )
            await ctx.send(message)

        else:
            # Use the last word in the input as the search term
            name = name.split()[-1]

            # Fetch player data by name
            player_data = fetch_player(name)
            if not player_data or not player_data["data"]:
                await ctx.send(f"No players found for '{name}'. Please try another name.")
                return

            players = player_data["data"]
            if len(players) == 1:
                # If only one player is found, display detailed info
                player = players[0]
                height = (
                    f"{player.get('height_feet', 'N/A')} ft {player.get('height_inches', 'N/A')} in"
                    if player.get('height_feet') or player.get('height_inches')
                    else "Height not available"
                )
                weight = f"{player.get('weight_pounds', 'N/A')} lbs"
                team = player['team']['full_name'] if player.get('team') else "Free Agent"
                message = (
                    f"**{player['first_name']} {player['last_name']}**\n"
                    f"Position: {player.get('position', 'N/A')}\n"
                    f"Team: {team}\n"
                    f"Height: {height}\n"
                    f"Weight: {weight}"
                )
                await ctx.send(message)
            else:
                # If multiple players are found, list their names with IDs
                message = "**Multiple players found:**\n"
                for player in players:
                    team = player['team']['full_name'] if player.get('team') else "Free Agent"
                    message += (
                        f"- ID: {player['id']} | {player['first_name']} {player['last_name']} "
                        f"({team})\n"
                    )
                message += "\nUse `!player <player_id>` to fetch a specific player by their ID."
                await ctx.send(message)

async def setup(bot):
    """Asynchronously add the cog to the bot."""
    await bot.add_cog(Players(bot))