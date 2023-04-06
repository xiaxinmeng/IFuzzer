import socket, ssl
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssl_sock = ssl.wrap_socket(s)
ssl_sock.connect(('www.verisign.com', 443))
file = ssl_sock.makefile('rb')
file.close()
ssl_sock.close()