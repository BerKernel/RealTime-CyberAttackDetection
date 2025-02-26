# train_model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib

def train_model():
    """
    Reads a CSV file from the 'data' directory, trains a Random Forest model,
    prints a classification report, and saves the model as 'model.pkl'.
    """
    # Load the dataset (adjust the filename if necessary)
    data = pd.read_csv("data/network_intrusion.csv")
    
    # Separate features (X) and the target (y). 
    # We assume 'label' indicates whether a record is an attack or normal.
    X = data.drop("label", axis=1)
    y = data["label"]
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )
    
    # Create and train the Random Forest model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Evaluate model performance
    y_pred = model.predict(X_test)
    report = classification_report(y_test, y_pred)
    print(report)
    
    # Save the trained model
    joblib.dump(model, "model.pkl")
    print("Model saved as model.pkl")

if __name__ == "__main__":
    train_model()
