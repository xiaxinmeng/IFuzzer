import socket
socket.socket(socket.SOCK_STREAM, socket.AF_INET)
s=socket.socket(socket.SOCK_STREAM, socket.AF_INET)
f=s.makefile("rb")
f.close()
print(repr(f))