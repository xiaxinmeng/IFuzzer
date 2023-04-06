#!/usr/bin/python3.2
# xmlclient.py
import xmlrpc.client
server_proxy = xmlrpc.client.ServerProxy("http://localhost:8000")
print(server_proxy.print_str("être à montréal"))

#!/usr/bin/python2.6
# xmlserve.py
from SimpleXMLRPCServer import SimpleXMLRPCServer
def print_str(s):
  return (repr(type(s)), repr(s)) 
server = SimpleXMLRPCServer(("localhost", 8000))
server.register_function(print_str)
server.serve_forever()