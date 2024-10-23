#!/usr/bin/python

import socket
import os
import sys
import signal

HOST = 'localhost'
PORT = 30001
data_payload = 2048
backlog = 5

def sigchld_handler(*args):
    pid, exit_code = os.wait()
    print ("Child pid %d exiting with code %d" % (pid, exit_code//256))

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


#signal.signal(signal.SIGCHLD, sigchld_handler)

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

    # Create new child
    p = os.fork()

    # We're child?
    if not p:
        client_handler(client)

        # Exit from child
        # Don't go to while True!
        sys.exit(1)



