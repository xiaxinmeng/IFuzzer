from xmlrpc.server import *

handler=CGIXMLRPCRequestHandler()
handler.register_introspection_functions()
handler.handle_request()