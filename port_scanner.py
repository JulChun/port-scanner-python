import socket
import sys

def scan_host(host, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((host, port))
            if result == 0:
                open_ports.append(port)
            sock.close()
        except KeyboardInterrupt:
            print("Interrupted by user.")
            sys.exit()
    return open_ports

if __name__ == "__main__":
    host = input("Enter host (e.g. 127.0.0.1): ")
    ports = scan_host(host, 75, 85)
    print(f"Open ports on {host}: {ports}")