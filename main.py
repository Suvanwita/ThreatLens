from monitor import follow
from parser import parse_log
from detector import detect
from alert import send_alert

LOG_FILE = "/var/log/auth.log"

def main():
    with open(LOG_FILE, "r") as file:
        loglines = follow(file)

        for line in loglines:
            print("RAW:", line)
            event = parse_log(line)

            if event:
                print("Parsed:", event)

                alerts = detect(event)

                for alert in alerts:
                    send_alert(alert)

if __name__ == "__main__":
    main()