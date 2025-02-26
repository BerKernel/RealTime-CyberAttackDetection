```md
# 🛡️ Real-Time Cyber Defense System

This project is an **open-source, real-time Intrusion Detection System (IDS)** that detects cyber attacks using **signature-based** and **machine learning-based** methods.

## 🚀 Features
✅ **Real-time network traffic monitoring**  
✅ **Hybrid detection system (Signature-based + ML-based)**  
✅ **Automated installation (Npcap & dependencies)**  
✅ **Real-time alert system (Sound & Email notifications)**  
✅ **Interactive UI with Streamlit**  
✅ **Logging & Reporting (Detection logs, visualization)**  

---

## 📥 Installation

To install all required dependencies and tools, run:
```bash
python install.py
```
This will:
- Automatically install **Npcap** (if not already installed)
- Install required **Python libraries** from `requirements.txt`

---

## 🎯 How to Use?

After installation, start the real-time detection system by running:
```bash
python main.py
```
This will:
- Start **network packet sniffing**
- Load **signature-based detection rules**
- Run **machine learning attack detection**
- Launch the **UI at** [`http://localhost:8501`](http://localhost:8501)

To access the **web-based UI** for real-time monitoring:
```bash
streamlit run ui.py
```

---

## 📊 Logging & Alerts

- **All detected attacks are logged in:** `logs/detections.log`
- **Alerts can be sent via email** (configured in `config.json`)

### 🔧 **Enable Email Alerts**
To receive email alerts for detected threats, update `config.json`:
```json
"email": {
  "enabled": true,
  "smtp_server": "smtp.gmail.com",
  "port": 587,
  "sender_email": "your_email@example.com",
  "receiver_email": "alert@example.com",
  "password": "your_app_password"
}
```
**Note:** If using **Gmail**, you may need to enable "Less secure apps" or use an **App Password**.

---

## 🛠️ Development & Contribution

We encourage contributions! You can:
- Add new **signature rules** in `rules/signature_rules.json`
- Improve **ML model training** in `train_model.py`
- Enhance **real-time anomaly detection logic**

If you'd like to contribute, fork this repository and submit a pull request. 🚀

---

## 📂 Project Structure

```
RealTime-CyberDefense/
│── config.json               # Configuration settings
│── install.py                # Automated installation (Npcap & dependencies)
│── main.py                   # Main script to start the detection system
│── train_model.py            # Machine learning model training
│── flow_capture.py           # Real-time network traffic capture
│── attack_detection.py       # Cyber attack detection (ML & Signature-based)
│── logger.py                 # Logging system
│── notifier.py               # Alert system (Sound & Email)
│── ui.py                     # Streamlit web-based UI
│── model/
│   ├── trained_model.pkl     # Pre-trained ML model
│   ├── signature_rules.json  # Signature-based detection rules
│── logs/
│   ├── detections.log        # Detected attack logs
│── requirements.txt          # Required Python libraries
└── LICENSE                   # MIT License
```

---

## 📝 License

This project is licensed under the **MIT License** – you're free to use, modify, and distribute it.

---

## 📧 Contact & Support

If you encounter any issues or have feature requests, feel free to open an issue on GitHub or reach out. 💬

