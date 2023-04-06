import socket
# address of server routable, but offline
server = "192.168.1.2"
s = socket.socket()
s.setblocking(1)
s.connect((server, 139))
s.close()