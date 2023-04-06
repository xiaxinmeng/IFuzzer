from SimpleXMLRPCServer import SimpleXMLRPCServer

server = SimpleXMLRPCServer(('127.0.0.1', 12345))
server.serve_forever()