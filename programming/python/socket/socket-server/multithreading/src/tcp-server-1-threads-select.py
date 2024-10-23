#!/usr/bin/python

import socket
import threading

HOST = 'localhost'
PORT = 30002
data_payload = 2048
backlog = 5

def client_handler(client):

    while True:
        data = client.recv(data_payload)

        if not data:
            break

        print("Data: %s" % data)
        s = client.send(data)
        print("sent %s bytes back" % (s,))

    # End connection
    client.close()

# Create a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Enable reuse address/port
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

print("Starting up echo server on %s port %s" % (HOST, PORT))
sock.bind((HOST, PORT))

# Listen to clients, backlog argument specifies the max no. of queued connections
sock.listen(backlog)

while True:
    print("Waiting to receive message from client")
    client, address = sock.accept()
    print("Client connected from %s" % (address,))

    # Create and start thread
    t = threading.Thread(target=client_handler, args=(client,))
    t.start()
