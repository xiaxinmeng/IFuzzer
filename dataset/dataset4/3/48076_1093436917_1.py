import socket
s=socket.socket()
s.connect(('www.python.org',80))
x=s.makefile()
x.close()
del s