import socket
import os
HEADER_SIZE = 10
rate = 14 + HEADER_SIZE + 6 # after encode length increase by 6

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        
    def receive_file(self):
        # Open a socket and connect to the server
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))
            
            # Receive the file name and size from the server
            file_info = s.recv(rate).decode()
            if not file_info:
                print('Error in receiving file name and size')
                exit(0)
            file_name, file_size = file_info.split(":")
            file_size = int(file_size)
            print(f'File info: name={file_name}, size={file_size}')
            
            # Receive the file data in chunks with sequence numbers
            received_data = ""
            expected_sequence_num = 0
            while len(received_data) < file_size:
                data = s.recv(rate).decode()
                if not data:
                    break
                if len(data) <= HEADER_SIZE:
                    continue  # Skip packets with no data
                sequence_num = int(data[:HEADER_SIZE])
                chunk = data[HEADER_SIZE:]
                if sequence_num == expected_sequence_num:
                    print(f'Packet No.{sequence_num}:\'{chunk}\'')

                    #  horizontal dividor for easy visual
                    divider = '-' * 50
                    print(divider)
                    
                    received_data += chunk
                    expected_sequence_num += 1
                else:
                    print(f"Packet loss detected: expected {expected_sequence_num}, got {sequence_num}")
            
            # Save the received file data to disk
            print('Completed transfering')


host = socket.gethostname() 
ip_address = socket.gethostbyname(host)

client = Client(ip_address, 1234)
client.receive_file()