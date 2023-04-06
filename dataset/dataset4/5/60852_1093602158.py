from socket import create_connection, SHUT_RDWR
from socketserver import TCPServer, BaseRequestHandler
from threading import Thread

server = TCPServer(("", 0), BaseRequestHandler)
Thread(target=server.serve_forever).start()
client = create_connection(server.server_address)
server.shutdown()  # Ensure server has closed client connection
server.server_close()
client.send(bytes(1))