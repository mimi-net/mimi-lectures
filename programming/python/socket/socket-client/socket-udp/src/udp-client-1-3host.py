import socket
import struct
import time
import select

NTP_SERVER1 = "1.ru.pool.ntp.org"
NTP_SERVER2 = "2.ru.pool.ntp.org"
NTP_SERVER3 = "3.ru.pool.ntp.org"
PORT = 123
TIME1970 = 2208988800

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

data = '\x1b' + 47 * '\0'

try:
    client.sendto( data.encode('utf-8'), (NTP_SERVER1, PORT))
    client.sendto( data.encode('utf-8'), (NTP_SERVER2, PORT))
    client.sendto( data.encode('utf-8'), (NTP_SERVER3, PORT))

    for i in range(3):
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