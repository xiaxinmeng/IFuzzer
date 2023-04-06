import socket
s = socket.socket()
s.connect('localhost', 5432)
S = s.makefile()