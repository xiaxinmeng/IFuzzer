import ssl
import xmlrpc.server

rpc_server = xmlrpc.server.SimpleXMLRPCServer(...)
ssl_context = ssl.SSLContext()
# setup the context ...
rpc_server.socket = ssl_context.wrap_socket(rpc_server.socket, ...)