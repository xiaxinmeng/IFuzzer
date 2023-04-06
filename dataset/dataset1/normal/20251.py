import socket
r, w = socket.socketpair()
w.send(b'X' * 1024)

buffer = bytearray()
r.recvfrom_into(buffer)
