import socket, ssl

sock = socket.socket()
sock.connect(('<FIRST_SERVER>', 443))
ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
sock = ctx.wrap_socket(sock)
sock.send(b'CONNECT <SECOND_SERVER>:443 HTTP/1.1\r\n\r\n')
print(sock.recv(1024))
ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
sock = ctx.wrap_socket(sock)
sock.do_handshake()
sock.send(b'CONNECT ifconf.me:80 HTTP/1.1\r\n\r\n')
print(sock.recv(1024))