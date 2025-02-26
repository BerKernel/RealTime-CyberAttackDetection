# tune_xgb.py

import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from xgboost import XGBClassifier
import joblib

def tune_xgb():
    data = pd.read_csv("data/flow_dataset.csv")  # Flow bazlı özellikler içeren CSV
    X = data.drop("label", axis=1)
    y = data["label"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

    param_grid = {
        "n_estimators": [50, 100],
        "max_depth": [3, 5, 10],
        "learning_rate": [0.01, 0.1, 0.2]
    }

    xgb = XGBClassifier(use_label_encoder=False, eval_metric='mlogloss')
    grid = GridSearchCV(xgb, param_grid, scoring="f1_macro", cv=3)
    grid.fit(X_train, y_train)

    print("Best Params:", grid.best_params_)
    print("Best Score:", grid.best_score_)

    best_model = grid.best_estimator_
    joblib.dump(best_model, "model/xgb_best.pkl")
    print("XGBoost best model saved.")

if __name__ == "__main__":
    tune_xgb()
