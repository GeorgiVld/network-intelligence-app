import socket
import subprocess
import platform
import re
import requests
import json

LOG_FILE = "output.json"

def get_active_connections():
    # Get active connections using netstat
    if platform.system() == "Windows":
        command = "netstat -an"
    else:
        command = "netstat -anp tcp"

    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    
    if process.returncode != 0:
        print("Error executing netstat command")
        print(stderr.decode())
        return []

    return stdout.decode()

def extract_ip_addresses(output):
    # Extract IP addresses from netstat output
    ip_addresses = re.findall(r'[0-9]+(?:\.[0-9]+){3}', output)
    return list(set(ip_addresses))  # Return unique IP addresses

def check_ip_threat(ip_address):
    # Check IP address against AbuseIPDB
    api_key = "a4f9d918ab31a60cc8de79c5b03a3a84bed930d9ffcac2d6d55663f5c63044a0d1b69a738b335f6c	"
    url = f"https://api.abuseipdb.com/api/v2/check?ipAddress={ip_address}"
    headers = {
        "Accept": "application/json",
        "Key": api_key
    }
    response = requests.get(url, headers=headers)
    return response.json()

def main():
    output = get_active_connections()
    ip_addresses = extract_ip_addresses(output)

    print("Active IP addresses:")
    for ip in ip_addresses:
        print(ip)

    results = []
    for ip in ip_addresses:
        threat_info = check_ip_threat(ip)
        result = {ip: threat_info}
        results.append(result)
    
    with open(LOG_FILE, "w") as f:
        json.dump(results, f, indent=4)
    
    print(f"Results written to {LOG_FILE}")
    
if __name__ == "__main__":
    main()
