import socket,sys
from thread import *
import time, random

HOST = '0.0.0.0'  # all IP can connect
PORT = 8989
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'

try:
    s.bind((HOST, PORT))
except socket.error, msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
print "Socket bind complete"

s.listen(10)  # 10 clients
print 'Socket now listening'

def clientThread(conn, clientaddress):
    while True:
        data = conn.recv(1024)
        if not data:
            break
        reply = 'server reply:\t' + data
        conn.sendall(reply)
    conn.close()

while 1:
    conn, addr = s.accept()
    clientaddress = addr[0] + ':' + str(addr[1])
    # print time.strftime("%Y/%m/%d %H:%M")+ '\t' + 'Connected with ' + clientaddress
    start_new_thread(clientThread, (conn, clientaddress))
s.close()
