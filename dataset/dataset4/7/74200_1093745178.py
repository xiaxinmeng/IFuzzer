import socket
sock = socket.socket()
sock.connect(('google.com', 80))
sock.setblocking(False)
print(sock.send(b'x' * 50000))
print(sock.send(b'x' * 50000))  # raise BlockingIOError