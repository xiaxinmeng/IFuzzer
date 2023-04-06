from socketserver import UnixStreamServer, StreamRequestHandler, ForkingMixIn


class Handler(StreamRequestHandler):
    def __init__(self, request, client_address, server):
        super().__init__(request, client_address, server)
        self.foo = 1

    def handle(self):
        print(self.foo)


class ThreadedUnixStreamServer(ForkingMixIn, UnixStreamServer):
    pass


with ThreadedUnixStreamServer("/tmp/test.socket", Handler) as server:
    server.serve_forever()