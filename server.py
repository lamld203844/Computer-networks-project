import socket

# create the socket
# AF_INET == ipv4
# SOCK_STREAM == TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific IP address and port
server_socket.bind(('localhost', 12345))

### incoming = listen for incoming connection (5 queues)
server_socket.listen(5)

print('Server listening for incoming connections...')

while True:
    # Accept a client connection
    client_socket, client_address = server_socket.accept()

    print(f'Connection from: {client_address}')

    # Send a message to the client
    client_socket.send(b'Hello from the server!')

    # Close the client socket
    client_socket.close()
