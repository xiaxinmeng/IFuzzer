class MySSLSocket(ssl.SSLSocket):
    pass

ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ctx.sslsocket_class = MySSLSocket
sock = ctx.wrap_socket(socket.socket(), server_side=True)
assert isinstance(sock, MySSLSocket)