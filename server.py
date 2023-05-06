import socket
import os

HEADER_SIZE = 10

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        
    def receive_file(self):
        # Open a socket and listen for connections
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            s.listen()
            conn, addr = s.accept()
            
            # Receive the file name and size from the client
            file_info = conn.recv(1024).decode()
            file_name, file_size = file_info.split(":")
            file_size = int(file_size)
            print(f'{file_name}, {file_size}')
            
            # Receive the file data in chunks with sequence numbers
            received_data = ""
            expected_sequence_num = 0
            while len(received_data) < file_size:
                data = conn.recv(1024).decode()
                if not data:
                    break
                sequence_num = int(data[:HEADER_SIZE])
                chunk = data[HEADER_SIZE:]
                if sequence_num == expected_sequence_num:
                    received_data += chunk
                    expected_sequence_num += 1
                else:
                    print(f"Packet loss detected: expected {expected_sequence_num}, got {sequence_num}")
            
            # Save the received file data to disk
            print('Received successfully')

host = socket.gethostname() 
ip_address = socket.gethostbyname(host)

server = Server(ip_address, 1234)
server.receive_file()