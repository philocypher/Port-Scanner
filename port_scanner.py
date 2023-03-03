import argparse
import socket

def scan_port(host, port):
    # Create a socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    # Connect to the server
    result = sock.connect_ex((host, port))

    # Close the socket
    sock.close()

    return result == 0

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Port scanner")
parser.add_argument("-host", help="the host to scan")
parser.add_argument("-p", "--ports", metavar="port_range", type=str,
                    help="the range of ports to scan (e.g. 1-1024)",
                    default="1-1024")
args = parser.parse_args()

# Parse port range
start_port, end_port = map(int, args.ports.split("-"))
ports = range(start_port, end_port + 1)

# Scan each port
for port in ports:
    if scan_port(args.host, port):
        print(f"Port {port} is open")
    else:
        print(f"Port {port} is closed")
