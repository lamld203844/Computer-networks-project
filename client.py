import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server on a specific IP address and port
flag = client_socket.connect(('localhost', 12345))

# Connect successfully
if flag == None:
    # init full data
    full_data = ''

    # receive stream
    while True:
        # Receive packet from the server 8 bytes at a time
        data = client_socket.recv(8)
        if len(data) <= 0:
            break
        full_data += data.decode('utf-8')
    if len(full_data) > 0:
        print(f'Received data: {full_data}')
else:
    print('Error connection')

# Close the client socket
client_socket.close()