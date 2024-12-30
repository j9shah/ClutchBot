import json
import pandas as pd

def preprocess_game_data(input_file, output_file):
    """
    Preprocess game data for ML training.
    Extract features like team stats, scores, and outcomes.
    """
    with open(input_file, "r") as f:
        games = json.load(f)
    
    data = []
    for game in games:
        home_team = game["home_team"]["full_name"]
        visitor_team = game["visitor_team"]["full_name"]
        home_score = game["home_team_score"]
        visitor_score = game["visitor_team_score"]
        outcome = 1 if home_score > visitor_score else 0  # 1 for home win, 0 for away win
        
        data.append({
            "home_team": home_team,
            "visitor_team": visitor_team,
            "home_score": home_score,
            "visitor_score": visitor_score,
            "outcome": outcome
        })
    
    df = pd.DataFrame(data)
    df.to_csv(output_file, index=False)
    print(f"Preprocessed data saved to {output_file}")

if __name__ == "__main__":
    preprocess_game_data("data/historical_games.json", "data/preprocessed_games.csv")