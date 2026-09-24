from pathlib import Path
import re


def analyze_nmap_file(filename="data/nmap_localhost.txt"):
    path = Path(filename)

    if not path.exists():
        return "Nmap report not found."

    text = path.read_text()

    print("=== NOVA NMAP ANALYSIS ===")

    found = False

    for line in text.splitlines():
        match = re.match(
            r"^\s*(\d+)/tcp\s+(\S+)\s+(\S+)(?:\s+(.*))?$",
            line
        )

        if not match:
            continue

        found = True
        port, state, service, version = match.groups()

        print(f"\nPort: {port}/tcp")
        print(f"State: {state}")
        print(f"Service: {service}")

        if version:
            print(f"Version: {version}")

        if state == "open":
            print("Explanation: A service is accepting connections on this port.")
        elif state == "closed":
            print("Explanation: The port is reachable, but no service is accepting connections.")
        elif state == "filtered":
            print("Explanation: A firewall or filtering mechanism may be blocking the scan.")

    if not found:
        print("No TCP port entries were found.")

    print("\n=== END ANALYSIS ===")


if __name__ == "__main__":
    analyze_nmap_file()
