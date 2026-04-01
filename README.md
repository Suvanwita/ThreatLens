# 🔍 ThreatLens – Mini SIEM in Python

A real-time log monitoring and threat detection system built in Python that simulates core features of a SIEM (Security Information and Event Management) tool.

The system continuously monitors Linux logs, parses security events, detects suspicious activity (like brute-force attacks), and triggers alerts instantly.

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
├── monitor.py # Real-time log reader
├── parser.py # Log parsing logic
├── detector.py # Threat detection engine
├── alert.py # Alert system
├── main.py # Main pipeline
├── attacker.py # Attack simulation bot
└── README.md
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

## 🔥 Attack Simulation Bot

The attacker.py script simulates:

- Random SSH login attempts
- Sudo privilege abuse
- Custom malicious logs
- High-volume attack traffic

---

## 🛠️ Installation

```bash
git clone https://github.com/Suvanwita/ThreatLens.git
cd ThreatLens
```

---

## ▶️ Usage

Run the system
```bash
sudo python3 main.py
```
Simulate attacks (in another terminal)
```bash
python3 attacker.py
```

---

## 📌 Tech Stack

- Python
- Linux Logs (/var/log/auth.log)
- Regex
- Shell Commands

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
