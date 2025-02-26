# server.py

import socket
import time
import csv

HOST = '127.0.0.1'
PORT = 65432

def run_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    print(f"Server is listening on port {PORT}")
    
    conn, addr = s.accept()
    print(f"Connection from {addr}")
    
    with open("data/network_intrusion.csv", "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader, None)  # Skip header if exists
        
        for row in reader:
            line = ",".join(row) + "\n"
            conn.sendall(line.encode("utf-8"))
            time.sleep(1)  # 1-second delay to emulate real-time streaming

    conn.close()

if __name__ == "__main__":
    run_server()
