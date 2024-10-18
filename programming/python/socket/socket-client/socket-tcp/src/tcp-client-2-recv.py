#!/usr/bin/python

import socket

HOST = "miminet.ru"
PORT = 80

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)

try:
    s.connect((HOST, PORT))
    data = s.recv(4096)
    print(data)
except Exception as e:
    print ("Socket error: " + str(e))