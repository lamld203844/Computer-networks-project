import socket
import os
import base64
import random

SEQ_SIZE = 10
ERROR_BYTE = 1 # 1 byte for error
HEADER_SIZE = SEQ_SIZE + ERROR_BYTE
rate = 14 # reading file rate

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sequence_num = 0

    def generate_error(self):
        # Generate a random number following a normal distribution
        random_number = random.gauss(0, 1)

        # Apply a threshold to convert the number to 0 or 1
        threshold = 0.5
        return 0 if random_number < threshold else 1


    def send_file(self, file_path):
        # Open a socket and listen for connections
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            s.listen()
            conn, addr = s.accept()
            print(f'Connection from {addr} is established')
            
            # Send the file name and size to the client
            file_name = os.path.basename(file_path)
            file_size = os.path.getsize(file_path)
            conn.sendall(f"{file_name}:{file_size}".encode())
            
            # Send the file data in chunks with sequence numbers
            with open(file_path, "rb") as f:
                while True:
                    binary_data = f.read(rate)
                    if not binary_data:
                        break

                    # Encrypt in specific format using Base64
                    encoded64_data = base64.b64encode(binary_data)
                    # string representation of bin data (can understanding directly)
                    data = encoded64_data.decode()

                    # add error element
                    error = self.generate_error()

                    packet = f"{self.sequence_num:<{SEQ_SIZE}}"+ f"{error:<{ERROR_BYTE}}" + data
                    conn.sendall(packet.encode())
                    self.sequence_num += 1

host = socket.gethostname() 
ip_address = socket.gethostbyname(host)

server = Server(ip_address, 1234)
server.send_file(os.getcwd()+'\hello.pdf')