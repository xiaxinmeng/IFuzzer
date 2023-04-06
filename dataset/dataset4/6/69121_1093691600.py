import socket
a, b = socket.socketpair(socket.AF_UNIX, socket.SOCK_DGRAM)
a.send(b'abcdefgh')
result = b.recv(2, socket.MSG_TRUNC)
print(len(result), result)