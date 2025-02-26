# capture/packet_parser.py

from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP

def packet_callback(packet):
    """
    Extract relevant features from each packet.
    Return a dictionary of features that the ML model can use.
    """
    features = {}
    
    if IP in packet:
        ip_layer = packet[IP]
        features["src_ip"] = ip_layer.src
        features["dst_ip"] = ip_layer.dst
        features["proto"] = ip_layer.proto  # 6 = TCP, 17 = UDP
    
    # Check if TCP or UDP
    if TCP in packet:
        tcp_layer = packet[TCP]
        features["src_port"] = tcp_layer.sport
        features["dst_port"] = tcp_layer.dport
    elif UDP in packet:
        udp_layer = packet[UDP]
        features["src_port"] = udp_layer.sport
        features["dst_port"] = udp_layer.dport
    
    return features

def start_capture(interface="eth0", count=0):
    """
    Start sniffing packets on the specified interface.
    'count=0' means capture indefinitely.
    """
    sniff(iface=interface, prn=packet_callback, count=count)
