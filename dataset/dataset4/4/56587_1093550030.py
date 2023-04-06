new_socket = socket.create_connection((host, port), timeout)
ssl_socket = ssl.wrap_socket(new_socket, self.keyfile, self.certfile, do_handshake_on_connect=False)
try:
    ssl_socket.do_handshake()
except:
    ssl_socket.close()
    new_socket.close()
    raise
self.file = SSLFakeFile(ssl_socket)
return ssl_socket