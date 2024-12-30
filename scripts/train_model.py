import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle

def train_model(input_file, model_file):
    """
    Train a Logistic Regression model to predict game outcomes.
    """
    # load preprocessed data
    df = pd.read_csv(input_file)
    
    # encode team names as categorical variables
    df["home_team"] = df["home_team"].astype("category").cat.codes
    df["visitor_team"] = df["visitor_team"].astype("category").cat.codes
    
    X = df[["home_team", "visitor_team"]]
    y = df["outcome"]
    
    # split into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # train model
    model = LogisticRegression()
    model.fit(X_train, y_train)
    
    # evaluate model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model accuracy: {accuracy * 100:.2f}%")
    
    # save model
    with open(model_file, "wb") as f:
        pickle.dump(model, f)
    print(f"Model saved to {model_file}")

if __name__ == "__main__":
    train_model("data/preprocessed_games.csv", "data/game_predictor.pkl")