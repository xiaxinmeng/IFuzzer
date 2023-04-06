import socket, ssl
with socket.socket() as sock:
    s = ssl.wrap_socket(sock,
                        ssl_version=ssl.PROTOCOL_TLSv1,
                        ciphers='SRP',
                        tls_username='jsmith',
                        tls_password='abc')
    s.connect(('tls-srp.test.trustedhttp.org', 443))
    s.write(b"GET / HTTP/1.0\n\n")
    print(s.read())