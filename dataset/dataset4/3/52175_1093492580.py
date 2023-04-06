import socket
import ssl
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sslsock = ssl.SSLSocket(sock)
assert sslsock._sslobj is None
sslsock.connect(('www.gmail.com', 443))
assert isinstance(sslsock._sslobj, socket._ssl.SSLType)
assert 0 == sslsock._makefile_refs
sslsock.makefile().close()
assert 1 == sslsock._makefile_refs  # Should be 0.
assert sslsock._sslobj is not None  # Should be None.