import socket
s=socket.socket(socket.AF_INET,socket.SOCK_RAW,4)
s.sendto("",("x.x.x.x",0))