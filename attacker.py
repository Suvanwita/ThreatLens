import os
import time
import random

def ssh_attack():
    users = ["admin", "root", "test", "guest"]
    user = random.choice(users)

    print(f"[ATTACK] Trying SSH login for {user}")
    os.system(f"ssh {user}@localhost")  # will fail

def sudo_attack():
    print("[ATTACK] Trying sudo abuse")
    os.system("sudo -k")  # force password prompt
    os.system("sudo ls")  # enter wrong password manually

def custom_attack():
    messages = [
        "Brute force attempt detected",
        "Multiple login failures",
        "Suspicious activity from unknown IP",
        "Unauthorized access attempt"
    ]
    msg = random.choice(messages)

    print(f"[ATTACK] Logging: {msg}")
    os.system(f'logger "{msg}"')

def run_bot():
    actions = [ssh_attack, sudo_attack, custom_attack]

    while True:
        attack = random.choice(actions)
        attack()

        sleep_time = random.randint(2, 5)
        time.sleep(sleep_time)

if __name__ == "__main__":
    run_bot()