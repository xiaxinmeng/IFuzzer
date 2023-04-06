import socket
import struct
import time

# first request
sock = socket.socket()
l_onoff = 1
l_linger = 0
sock.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER, struct.pack('ii', l_onoff, l_linger))
sock.connect(('127.0.0.1', 8022))
sock.close()

time.sleep(1)

# second request
sock = socket.socket()
sock.connect(('127.0.0.1', 8888))
print('Got', sock.recv(1024))
sock.sendall(b'Hi there')
print('Got', sock.recv(1024))  # <-- Will hang here
sock.close()