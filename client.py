import socket
import os
HEADER_SIZE = 10

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sequence_num = int(0)
        
    def send_file(self, file_path):
        # Open a socket and connect to the server
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))
            
            # Send the file name and size to the server
            file_name = os.path.basename(file_path)
            file_size = os.path.getsize(file_path)
            s.sendall(f"{file_name}:{file_size}".encode())
            
            # Send the file data in chunks with sequence numbers
            with open(file_path, "r") as f:
                while True:
                    data = f.read(1024)
                    if not data:
                        break
                    packet = f"{self.sequence_num:<{HEADER_SIZE}}" + data
                    s.sendall(packet.encode())
                    self.sequence_num += 1

host = socket.gethostname() 
ip_address = socket.gethostbyname(host)

client = Client(ip_address, 1234)
client.send_file(os.getcwd()+'\hello.pdf')