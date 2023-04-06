import SocketServer
class RequestHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        self.request.send("")
server = SocketServer.TCPServer(("localhost", 2000),
RequestHandler)
server.serve_forever()