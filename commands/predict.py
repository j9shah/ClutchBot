import discord
from discord.ext import commands
import pickle
import pandas as pd

class Predict(commands.Cog):
    """Game prediction command."""

    def __init__(self, bot):
        self.bot = bot
        # load trained model
        with open("data/game_predictor.pkl", "rb") as f:
            self.model = pickle.load(f)
        # map of team names to numerical encodings (from training data)
        self.team_mapping = self._get_team_mapping()

    def _get_team_mapping(self):
        """
        Create a mapping of team names to numerical encodings based on training data.
        """
        df = pd.read_csv("data/preprocessed_games.csv")
        home_teams = df["home_team"].astype("category").cat.categories
        return {team: idx for idx, team in enumerate(home_teams)}

    def _find_team(self, partial_name):
        """
        Find a team by partial name match.
        """
        matches = [team for team in self.team_mapping.keys() if partial_name.lower() in team.lower()]
        return matches

    @commands.command()
    async def predict(self, ctx, team1: str, team2: str):
        """
        Predict the outcome of a game between two teams.
        Usage: !predict <team1> <team2>
        """
        try:
            team1_matches = self._find_team(team1)
            team2_matches = self._find_team(team2)

            if len(team1_matches) == 0 or len(team2_matches) == 0:
                await ctx.send(
                    f"One or both of the teams ('{team1}', '{team2}') are not recognized. "
                    f"Please check the names and try again."
                )
                return

            if len(team1_matches) > 1 or len(team2_matches) > 1:
                await ctx.send(
                    f"Multiple matches found for one or both teams:\n"
                    f"**{team1}** matches: {', '.join(team1_matches)}\n"
                    f"**{team2}** matches: {', '.join(team2_matches)}\n"
                    f"Please refine your input."
                )
                return

            team1_full = team1_matches[0]
            team2_full = team2_matches[0]

            team1_encoded = self.team_mapping[team1_full]
            team2_encoded = self.team_mapping[team2_full]

            X = [[team1_encoded, team2_encoded]]
            prob = self.model.predict_proba(X)[0]  # probability of [team1 win, team2 win]

            response = (
                f"Prediction for {team1_full} vs {team2_full}:\n"
                f"**{team1_full}** win probability: {prob[1] * 100:.2f}%\n"
                f"**{team2_full}** win probability: {prob[0] * 100:.2f}%"
            )
            await ctx.send(response)

        except Exception as e:
            await ctx.send("An error occurred while processing your request. Please try again later.")
            # log the error for debugging purposes
            print(f"Error in !predict command: {e}")

async def setup(bot):
    """Asynchronously add the cog to the bot."""
    await bot.add_cog(Predict(bot))