import requests
from dotenv import load_dotenv
import os

API_KEY = os.getenv("API_KEY")
HEADERS = {"Authorization": API_KEY}

BASE_URL = "https://api.balldontlie.io/v1"

def fetch_scores(date):
    """Fetch NBA games and scores for a specific date."""
    url = f"{BASE_URL}/games?dates[]={date}"
    response = requests.get(url, headers=HEADERS)
    return response.json() if response.status_code == 200 else None

def fetch_player(query):
    """
    Fetch a player by name or ID.
    If the query is an integer, treat it as an ID.
    """
    try:
        if query.isdigit():  # If the query is numeric, treat it as an ID
            url = f"{BASE_URL}/players/{query}"
            response = requests.get(url, headers=HEADERS)
            if response.status_code == 200:
                # Return the "data" object when querying by ID
                return response.json().get("data", None)
            else:
                return None
        else:  # Otherwise, treat it as a name search
            url = f"{BASE_URL}/players?search={query}"
            response = requests.get(url, headers=HEADERS)
            return response.json() if response.status_code == 200 else None
    except Exception as e:
        print(f"Error fetching player: {e}")
        return None

def fetch_teams():
    """Fetch all NBA teams."""
    url = f"{BASE_URL}/teams"
    response = requests.get(url, headers=HEADERS)
    return response.json() if response.status_code == 200 else None