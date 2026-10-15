import socket
def echo_server():
 # Create a TCP/IP socket
 server_socket = socket.socket(socket.AF_INET,
 socket.SOCK_STREAM)
 # Bind the socket to a specific address and port
 server_socket.bind(('localhost', 65432))
 # Listen for incoming connections
 server_socket.listen(1)
 print("Server listening on port 65432...")
 connection, client_address = server_socket.accept()
 print(f"Connected by {client_address}")
 while True:
     data = connection.recv(1024)
     if not data:
         break
     print(f"Received: {data.decode()}")
     connection.sendall(data)
 connection.close()
if __name__ == '__main__':
 echo_server()