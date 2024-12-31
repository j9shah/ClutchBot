# ClutchBot | Discord Bot

## Introduction 🎮🏀📊

ClutchBot is a Discord bot built to deliver NBA data and game predictions directly to your server. From recent game scores and detailed player stats to predicting game outcomes, ClutchBot is your all-in-one basketball companion. Powered by a machine learning model trained on historical NBA data, the bot provides accurate insights for basketball fans and enthusiasts. 🌟

### Key Features

- Fetch recent NBA game scores.
- Provide detailed player statistics.
- List all NBA teams.
- Predict game outcomes using historical data and machine learning.

## Tools & Technologies 🛠️📚🤖

- **Python**: Core programming language.
- **Discord.py**: Framework for bot development.
- **scikit-learn**: Algorithm for predictions.
- **Pandas**: Data preprocessing and analysis.
- **balldontlie API**: NBA data source.

---

![image](https://github.com/user-attachments/assets/7deba7bf-b08a-4a06-8238-5d331a019679)

![image](https://github.com/user-attachments/assets/d4491f66-a1a1-4c2f-af7d-43535c5b087f)

![image](https://github.com/user-attachments/assets/b87b7e33-c774-44aa-8ebc-29603c5cd617)

---

## Features 🏆✨🎯

- **Fetch Scores**: Use `!scores` or `!games` to get the latest NBA game results.

- **Player Details**: Use `!players <name>` to retrieve information about a player.

- **Team Listings**: Use `!teams` to list all NBA teams.

- **Game Predictions**: Use `!predict <team1> <team2>` to predict the outcome of a matchup.

- **Future Capabilities**: In the future, the bot will be able to fetch current injuries, player stats, and other real-time data for enhanced predictions.

  &#x20;

## Commands 💻🗒️🎮

1. **`!scores`**\*\* or \*\*\*\*`!games`\*\*:
   Fetch recent NBA game scores.

   ```plaintext
   !scores
   ```

2. **`!teams`**:
   List all NBA teams.

   ```plaintext
   !teams
   ```

3. **`!players <name>`**:
   Fetch details about an NBA player.

   ```plaintext
   !players LeBron
   ```

4. **`!predict <team1> <team2>`**:
   Predict the outcome of a game using a machine learning model.

   ```plaintext
   !predict Lakers Warriors
   ```

## Model Overview 🧠📈🤔

The prediction model leverages historical NBA game data to estimate game outcomes. Using logistic regression, it analyzes team stats like points scored, win/loss ratios, and game metadata such as home or away status. Key highlights include:

- Accuracy: The model achieves an accuracy of 68.33% on test data.
- Integration: Predictions are seamlessly integrated into the bot and can be accessed via the `!predict` command.
- Insights: Provides actionable predictions for basketball fans and enthusiasts. 📊✨

### Next Steps for Improvement 🛠️🎯🚀

1. **Enhanced Features**:

   - Add recent win/loss streaks.
   - Incorporate player stats, injuries, or roster changes.
   - Consider home-court advantage and team standings.

2. **Model Refinement**:

   - Experiment with advanced models like Random Forest or Gradient Boosting.
   - Use hyperparameter tuning to boost accuracy.

3. **Dynamic Predictions**:

   - Include live stats before generating predictions.
   - Adjust predictions based on real-time factors such as injuries.

4. **Evaluation Metrics**:

   - Implement precision/recall and confusion matrix for better performance tracking. 🎯📈✅
