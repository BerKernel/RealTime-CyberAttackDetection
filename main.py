import threading
from detection.flow_capture import start_sniffing
from detection.realtime_detection import detect_attack
from app import start_ui

if __name__ == "__main__":
    print("Starting Cyber Defense System...")
    sniffing_thread = threading.Thread(target=start_sniffing)
    sniffing_thread.start()

    ui_thread = threading.Thread(target=start_ui)
    ui_thread.start()
