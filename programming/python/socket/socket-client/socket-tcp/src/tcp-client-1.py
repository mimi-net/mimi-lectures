#!/usr/bin/python

import socket

HOST = "miminet.ru"                                     # miminet.ru
PORT = 80                                               # HTTP port

ip_addr = socket.gethostbyname(HOST)                    # Get IP address by name
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # Create TCP socket
s.connect((ip_addr, PORT))                              # Connect to miminet.ru
s.send(b'GET / HTTP/1.0\n\n')                           # Send HTTP-request
data = s.recv(4096)                                     # Recieve data from miminet.ru
print(data)                                             # Print data to console
