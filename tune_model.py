# tune_model.py

import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
import joblib

def tune_model():
    data = pd.read_csv("data/nsl_kdd.csv")
    X = data.drop("label", axis=1)
    y = data["label"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

    param_grid = {
        "n_estimators": [50, 100],
        "max_depth": [None, 10, 20],
        "min_samples_split": [2, 5]
    }

    rf = RandomForestClassifier(random_state=42)
    grid = GridSearchCV(rf, param_grid, scoring="f1_macro", cv=3)
    grid.fit(X_train, y_train)

    print("Best Params:", grid.best_params_)
    print("Best Score:", grid.best_score_)

    best_model = grid.best_estimator_
    joblib.dump(best_model, "model/tuned_model.pkl")
    print("Tuned model saved to model/tuned_model.pkl")

if __name__ == "__main__":
    tune_model()
