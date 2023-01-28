import socket

def scan(host, port):
    try:
        s = socket.socket()
        s.connect((host, port))
        return True
    except:
        return False

for port in range(1, 65535):
    if scan("example.com", port):
        print("Port", port, "is open.")