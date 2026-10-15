import socket
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
print("Host Name:",hostname)
print("Ip Address:",ip_address)