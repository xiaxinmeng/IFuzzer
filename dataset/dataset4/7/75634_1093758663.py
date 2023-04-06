ctx = ssl.SSLContext(ssl.PROTOCOL_TLS)
ctx.load_cert_chain('server.pem')
ctx.options &= ~(ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1)

sslsock = ctx.wrap_socket(s, server_side=True)