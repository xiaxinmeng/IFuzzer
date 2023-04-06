import socket, ssl

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('www.verisign.com', 80))
s.close()
s.recv(1024)