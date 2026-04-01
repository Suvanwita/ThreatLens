# 🔍 ThreatLens – Mini SIEM in Python

**ThreatLens** is a lightweight Security Information and Event Management (SIEM) tool built in Python.
It monitors system logs, parses critical information, detects suspicious activities, and generates real-time alerts.

> 🚀 A simplified, developer-friendly version of enterprise SIEM tools.

---

## 🧠 Features

* 📡 **Log Monitoring** – Continuously reads system logs
* 🧾 **Log Parsing** – Extracts IPs, timestamps, and actions
* 🚨 **Threat Detection** – Identifies suspicious patterns (e.g., failed logins)
* 🔔 **Alert System** – Notifies when anomalies are detected
* ⚡ **Modular Design** – Clean, scalable architecture

---

## 🏗️ Project Structure

```
ThreatLens/
│
├── monitor.py    # Reads and streams logs
├── parser.py     # Extracts structured data from logs
├── detector.py   # Applies detection logic (rules/anomalies)
├── alert.py      # Handles alerting (console/email/etc.)
├── main.py       # Entry point of the application
└── utils.py      # Helper functions
```

---

## ⚙️ How It Works

```
Logs → Monitor → Parser → Detector → Alert
```

1. **Monitor** reads logs in real-time
2. **Parser** extracts useful fields
3. **Detector** identifies threats
4. **Alert** notifies the user

---

## 🛠️ Installation

```bash
git clone https://github.com/Suvanwita/ThreatLens.git
cd ThreatLens
pip install -r requirements.txt
```

---

## ▶️ Usage

```bash
python main.py
```

---

## 🎯 Tech Stack

* Python
* Regex (for parsing)
* Basic rule-based detection

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork this repo and submit a pull request.

---

## 📜 License

This project is open-source and available under the MIT License.

---

## ⭐ Acknowledgment

Inspired by real-world SIEM systems used in cybersecurity operations.
