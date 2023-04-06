import socket

sock1 = socket.create_connection(('::1', '80'))
sock2 = socket.create_connection(sock1.getpeername())