import socket, time

while 1:
    res = socket.getaddrinfo('localhost', 80, 0,
socket.SOCK_STREAM)
    time.sleep(0.01)