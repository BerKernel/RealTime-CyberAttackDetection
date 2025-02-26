# hybrid_detection.py

import json
import joblib
import pandas as pd
from scapy.all import sniff, IP, TCP, UDP

def load_signature_rules():
    with open("rules/signature_rules.json", "r") as f:
        return json.load(f)

def check_signatures(features, rules):
    """
    Basit kural eşleştirme: 
    - rule["src_ip"] != None ise features["src_ip"] ile eşleşmeli
    - rule["dst_port"] != None ise features["dst_port"] ile eşleşmeli
    """
    for rule in rules:
        match_src = (rule["src_ip"] is None or rule["src_ip"] == features.get("src_ip"))
        match_dst = (rule["dst_port"] is None or rule["dst_port"] == features.get("dst_port"))
        if match_src and match_dst:
            return rule["rule_name"]
    return None

def packet_handler(packet, model, rules):
    feats = {
        "src_ip": None,
        "dst_ip": None,
        "src_port": 0,
        "dst_port": 0,
        "proto": 0
    }

    if IP in packet:
        ip_layer = packet[IP]
        feats["src_ip"] = ip_layer.src
        feats["dst_ip"] = ip_layer.dst
        feats["proto"] = ip_layer.proto

    if TCP in packet:
        feats["src_port"] = packet[TCP].sport
        feats["dst_port"] = packet[TCP].dport
    elif UDP in packet:
        feats["src_port"] = packet[UDP].sport
        feats["dst_port"] = packet[UDP].dport

    # 1) Signature check
    signature_alert = check_signatures(feats, rules)
    if signature_alert:
        print(f"Signature ALERT: {signature_alert}")
        return

    # 2) ML check
    df = pd.DataFrame([{
        "proto": feats["proto"],
        "src_port": feats["src_port"],
        "dst_port": feats["dst_port"]
    }])
    pred = model.predict(df)[0]
    if pred != "normal":
        print(f"ML ALERT: {pred}")

def start_hybrid_detection(interface="Ethernet"):
    model = joblib.load("model/trained_model.pkl")
    rules = load_signature_rules()
    sniff(iface=interface, prn=lambda p: packet_handler(p, model, rules))

if __name__ == "__main__":
    start_hybrid_detection()
