# main.py

import streamlit as st
import socket
import joblib
import pandas as pd
import time

HOST = '127.0.0.1'
PORT = 65432

def main():
    st.title("Real-Time Anomaly/Intrusion Detection (Live)")

    st.write("""
    This application receives data from a local socket server (server.py)
    and applies a pre-trained model to detect anomalies or intrusions.
    """)

    try:
        model = joblib.load("model.pkl")
        st.success("Model loaded successfully.")
    except:
        st.error("Could not find 'model.pkl'. Please train the model first.")
        return

    if st.button("Start Listening"):
        st.info("Listening on socket for incoming data...")

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        st.write("Connected to the server.")

        while True:
            data = s.recv(1024)
            if not data:
                st.write("No more data. Closing connection.")
                s.close()
                break
            
            lines = data.decode("utf-8").split("\n")
            for line in lines:
                if line.strip() == "":
                    continue
                
                values = line.split(",")
                # Assuming the last column is the label
                # and the rest are features
                X_values = values[:-1]
                actual_label = values[-1]

                try:
                    X_floats = [float(x) for x in X_values]
                except:
                    continue

                df = pd.DataFrame([X_floats])
                prediction = model.predict(df)[0]

                if prediction == "normal":
                    st.write(f"Data: {X_values} => Prediction: **Normal** (Actual: {actual_label})")
                else:
                    st.write(f"Data: {X_values} => Prediction: **Attack/Anomaly** (Actual: {actual_label})")

                time.sleep(0.5)  # small delay for display

if __name__ == "__main__":
    main()
