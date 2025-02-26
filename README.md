# Real-Time (Simulated) Anomaly/Intrusion Detection

This project demonstrates how to train a machine learning model (Random Forest) on a network intrusion dataset (e.g., from [Kaggle](https://www.kaggle.com/datasets/chethuhn/network-intrusion-dataset)) and perform **real-time** or **simulated real-time** anomaly/attack detection using a **Streamlit** interface.

## Features

- **Model Training:** A Python script (`train_model.py`) that trains a Random Forest classifier on the dataset and saves the model to `model.pkl`.
- **Real-Time Detection:** A Streamlit-based application (`main.py`) that processes rows from the dataset one by one, displaying prediction results in real time.
- **Easy Setup:** Uses a `requirements.txt` file to list all necessary Python dependencies.

## Project Structure

