# app.py

import streamlit as st
import threading
import time
import joblib
import pandas as pd
from scapy.all import sniff, IP, TCP, UDP

def packet_handler(packet, model):
    features = {
        "proto": 0,
        "src_port": 0,
        "dst_port": 0
    }
    if IP in packet:
        features["proto"] = packet[IP].proto
    if TCP in packet:
        features["src_port"] = packet[TCP].sport
        features["dst_port"] = packet[TCP].dport
    elif UDP in packet:
        features["src_port"] = packet[UDP].sport
        features["dst_port"] = packet[UDP].dport

    df = pd.DataFrame([features])
    pred = model.predict(df)[0]

    # Burada st.session_state veya global bir listeye kaydedebiliriz
    if pred != "normal":
        # Saldırı/anomali
        msg = {
            "time": time.strftime("%H:%M:%S"),
            "proto": features["proto"],
            "src_port": features["src_port"],
            "dst_port": features["dst_port"],
            "label": pred
        }
        st.session_state.alerts.append(msg)

def start_sniff(interface, model):
    sniff(iface=interface, prn=lambda p: packet_handler(p, model))

def main():
    st.title("Real-Time Anomaly Detection (Advanced)")
    interface = st.text_input("Network Interface", value="Ethernet")

    if 'alerts' not in st.session_state:
        st.session_state.alerts = []

    if st.button("Start Detection"):
        st.info("Starting detection in a separate thread...")
        thread = threading.Thread(
            target=start_sniff,
            args=(interface, joblib.load("model/trained_model.pkl"))
        )
        thread.daemon = True
        thread.start()

    st.subheader("Alerts Table")
    # alerts tablosunu göster
    df_alerts = pd.DataFrame(st.session_state.alerts)
    st.dataframe(df_alerts)

    # Basit bir bar chart örneği (hangi label kaç kez?)
    if not df_alerts.empty:
        chart_data = df_alerts["label"].value_counts().rename_axis("label").reset_index(name="count")
        st.bar_chart(data=chart_data, x="label", y="count")

    time.sleep(2)  # 2 saniye bekleyip arayüzü yenile
    st.experimental_rerun()

if __name__ == "__main__":
    main()
