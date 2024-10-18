import socket
import struct
import time
import select

NTP_SERVER = "miminet.ru"
PORT = 125
TIME1970 = 2208988800

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

data = '\x1b' + 47 * '\0'

try:
    client.connect((NTP_SERVER, PORT))
    client.send( data.encode('utf-8'))

    rdy = select.select([client], [], [], 0.9)

    if not rdy[0]:
        raise RuntimeError("socket recv broken")

    data = client.recv(1024)

    if data:
        t = struct.unpack( '!12I', data)[8]
        t -= TIME1970
        print ('\tTime=%s' % time.ctime(t))
except Exception as e:
    print ("Socket error: " + str(e))