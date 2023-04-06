ctx = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
ctx.set_tlsext_host_name("foo.bar")
skt = ctx.wrap_socket(socket.socket())
skt.connect("bar.baz")