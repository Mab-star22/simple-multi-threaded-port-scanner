import socket
from datetime import datetime

# Target host to scan
target = input("Enter IP or website to scan (e.g. 127.0.0.1 or scanme.nmap.org): ")

# List of common ports high school CS projects usually check
ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 3306, 3389, 8080]

try:
    # Resolve domain name to IP address
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print(f"[-] Error: Could not resolve hostname '{target}'.")
    exit()

print("=" * 50)
print(f"Starting port scan on target: {target} ({target_ip})")
print(f"Time started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("=" * 50)

open_ports_count = 0

for port in ports:
    try:
        # Create a basic TCP socket connection
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.0)
        
        # connect_ex returns 0 if connection succeeds
        result = s.connect_ex((target_ip, port))
        
        if result == 0:
            # Try getting service name (like HTTP for port 80)
            try:
                service = socket.getservbyport(port, "tcp")
            except:
                service = "unknown service"
                
            print(f"[+] Port {port:<5} is OPEN! ({service})")
            open_ports_count += 1
        else:
            print(f"[-] Port {port:<5} is closed")
            
        s.close()
    except Exception as e:
        print(f"Error scanning port {port}: {e}")

print("=" * 50)
print(f"Scan complete! Found {open_ports_count} open port(s).")
print("Done scanning!")
