# train_model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib

def train_model():
    """
    Train a Random Forest model on a labeled dataset (e.g., NSL-KDD)
    and save the trained model as 'trained_model.pkl'.
    """
    data = pd.read_csv("data/nsl_kdd.csv")  # Example dataset
    X = data.drop("label", axis=1)
    y = data["label"]  # e.g., "normal" or "attack"

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    report = classification_report(y_test, y_pred)
    print(report)

    joblib.dump(model, "model/trained_model.pkl")
    print("Model saved to model/trained_model.pkl")

if __name__ == "__main__":
    train_model()
