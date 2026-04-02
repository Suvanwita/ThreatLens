from collections import defaultdict

ip_attempts = defaultdict(int)

def detect(event):
    alerts = []

    # SSH brute force
    if event["type"] == "ssh" and event["action"] == "Failed password":
        ip = event["ip"]
        ip_attempts[ip] += 1

        if ip_attempts[ip] == 5:
            alerts.append(f"SSH Brute-force from {ip}")

    # SUDO attack detection
    if event["type"] == "sudo":
        alerts.append("Suspicious sudo authentication failure")

    return alerts