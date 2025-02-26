# flow_capture.py

import time
import threading
from scapy.all import sniff, IP, TCP, UDP

# Flow table: { (src_ip, dst_ip, src_port, dst_port, proto): { 'packet_count': X, 'byte_count': Y, 'first_time': T1, 'last_time': T2, ... } }
flow_table = {}

LOCK = threading.Lock() 

def update_flow(packet):
    with LOCK:
        if IP in packet:
            ip_layer = packet[IP]
            src_ip = ip_layer.src
            dst_ip = ip_layer.dst
            proto = ip_layer.proto
        else:
            return

        if TCP in packet:
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
        elif UDP in packet:
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport
        else:
            # Sadece TCP/UDP'ye odaklanıyoruz
            src_port = 0
            dst_port = 0

        key = (src_ip, dst_ip, src_port, dst_port, proto)

        pkt_len = len(packet)

        now = time.time()
        if key not in flow_table:
            flow_table[key] = {
                'packet_count': 1,
                'byte_count': pkt_len,
                'first_time': now,
                'last_time': now
            }
        else:
            flow_table[key]['packet_count'] += 1
            flow_table[key]['byte_count'] += pkt_len
            flow_table[key]['last_time'] = now

def packet_callback(packet):
    update_flow(packet)

def start_flow_capture(interface="Ethernet"):
    sniff(iface=interface, prn=packet_callback)
