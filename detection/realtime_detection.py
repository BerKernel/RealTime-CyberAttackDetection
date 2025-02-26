# realtime_detection.py

import joblib
import json
import pandas as pd
from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP

def load_model():
    model = joblib.load("model/trained_model.pkl")
    return model

def load_signature_rules():
    with open("rules/signature_rules.json", "r") as f:
        rules = json.load(f)
    return rules

def check_signatures(packet_features, rules):
    """
    Compare packet_features with signature rules.
    If any rule matches, return an alert message.
    """
    for rule in rules:
        src_ip_match = (rule["src_ip"] is None or rule["src_ip"] == packet_features.get("src_ip"))
        dst_port_match = (rule["dst_port"] is None or rule["dst_port"] == packet_features.get("dst_port"))
        
        if src_ip_match and dst_port_match:
            return f"Signature alert: {rule['rule_name']}"
    return None

def packet_handler(packet, model, rules):
    # Extract features
    features = {}
    if IP in packet:
        ip_layer = packet[IP]
        features["src_ip"] = ip_layer.src
        features["dst_ip"] = ip_layer.dst
        features["proto"] = ip_layer.proto

    if TCP in packet:
        tcp_layer = packet[TCP]
        features["src_port"] = tcp_layer.sport
        features["dst_port"] = tcp_layer.dport
    elif UDP in packet:
        udp_layer = packet[UDP]
        features["src_port"] = udp_layer.sport
        features["dst_port"] = udp_layer.dport

    # Check signature-based rules
    signature_alert = check_signatures(features, rules)
    if signature_alert:
        print(signature_alert)
        return
    
    # Convert features to DataFrame row (dummy example)
    # Real model training requires consistent feature columns
    df = pd.DataFrame([{
        "proto": features.get("proto", 0),
        "src_port": features.get("src_port", 0),
        "dst_port": features.get("dst_port", 0),
        # Add more features as needed
    }])

    # ML prediction
    pred = model.predict(df)[0]
    if pred != "normal":
        print(f"ML alert: Detected {pred} traffic")

def start_realtime_detection(interface="eth0"):
    model = load_model()
    rules = load_signature_rules()

    sniff(iface=interface, prn=lambda x: packet_handler(x, model, rules))

if __name__ == "__main__":
    start_realtime_detection()
