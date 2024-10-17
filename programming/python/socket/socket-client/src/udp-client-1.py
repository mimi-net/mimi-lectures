import socket
import struct
import time
import select

NTP_SERVER = "2.ru.pool.ntp.org"
PORT = 123
TIME1970 = 2208988800

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

data = '\x1b' + 47 * '\0'

try:
    client.sendto( data.encode('utf-8'), (NTP_SERVER, PORT))
    rdy = select.select([client], [], [], 0.9)

    if not rdy[0]:
        raise RuntimeError("socket recv broken")

    data, address = client.recvfrom(1024)

    if data:
        print ('Response received from:', address)
        t = struct.unpack( '!12I', data)[8]
        t -= TIME1970
        print ('\tTime=%s' % time.ctime(t))
except Exception as e:
    print ("Socket error: " + str(e))