import requests
import json
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

# load the API key from the .env file
load_dotenv()
API_KEY = os.getenv("API_KEY")

BASE_URL = "https://api.balldontlie.io/v1/games"

def fetch_games_paginated(start_date, end_date):
    """
    Fetch historical game data between two dates using pagination.
    """
    games = []
    page = 1
    while True:
        url = f"{BASE_URL}?start_date={start_date}&end_date={end_date}&page={page}&per_page=100"
        headers = {"Authorization": API_KEY}
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"Error fetching data: {response.status_code}")
            break
        data = response.json()
        games.extend(data["data"])
        if not data["meta"]["next_cursor"]:  # no more pages
            break
        page += 1
    return games

def save_games_to_file(games, filename):
    """
    Save game data to a JSON file.
    """
    with open(filename, "w") as f:
        json.dump(games, f, indent=4)
    print(f"Saved {len(games)} games to {filename}")

if __name__ == "__main__":
    start_date = "2023-10-01"  # start of the 2023-2024 NBA season
    end_date = "2024-06-30"    # end of the 2023-2024 NBA season
    print(f"Fetching games from {start_date} to {end_date}...")
    games = fetch_games_paginated(start_date, end_date)
    save_games_to_file(games, "data/historical_games.json")