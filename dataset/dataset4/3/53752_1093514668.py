import socket
sock_a, sock_b = socket.socketpair()
sock_a = socket.socket(_sock=sock_a)
sock_b.close()
file_a = sock_a.makefile('w')
file_a.write('x')
file_a.flush()