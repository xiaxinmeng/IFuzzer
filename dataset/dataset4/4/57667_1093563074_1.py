import ssl, socket
sock = ssl.wrap_socket(socket.socket(), cert_reqs=ssl.CERT_REQUIRED)
sock.connect(('localhost', 443))
for i in range(100000):
    x=sock._sslobj.peer_certificate()