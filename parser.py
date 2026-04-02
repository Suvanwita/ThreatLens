import re

# SSH pattern
ssh_pattern = re.compile(
    r'(\w{3}\s+\d+\s[\d:]+).*?(Failed password|Accepted password).*?(?:user\s(\w+)|invalid user\s(\w+)).*?from\s([\d\.]+)'
)

def parse_log(line):

    # SSH logs
    ssh_match = ssh_pattern.search(line)
    if ssh_match:
        timestamp = ssh_match.group(1)
        action = ssh_match.group(2)
        user = ssh_match.group(3) if ssh_match.group(3) else ssh_match.group(4)
        ip = ssh_match.group(5)

        return {
            "type": "ssh",
            "timestamp": timestamp,
            "action": action,
            "user": user,
            "ip": ip
        }

    # SUDO FAILED AUTH
    if "sudo" in line and "authentication failure" in line:
        return {
            "type": "sudo",
            "timestamp": line.split()[0],
            "action": "sudo_auth_failure",
            "user": "unknown",
            "ip": "local"
        }

    # SUDO MULTIPLE FAIL ATTEMPTS
    if "incorrect password attempts" in line:
        return {
            "type": "sudo",
            "timestamp": line.split()[0],
            "action": "multiple_failed_sudo",
            "user": "unknown",
            "ip": "local"
        }

    return None