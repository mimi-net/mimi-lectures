import socket

HOST = ''
PORT = 30000
data_payload = 2048

# Create a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Starting up UDP echo server on %s port %s" % (HOST, PORT))
sock.bind((HOST, PORT))

while True:
    print("Waiting to receive message from client")
    data, address = sock.recvfrom(data_payload)

    if not data:
        continue

    print("Received %s bytes from %s" % (len(data), address))
    s = sock.sendto(data, address)
    print("Sent %s bytes back" % (s,))