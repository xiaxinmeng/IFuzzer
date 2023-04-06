import xmlrpc.client

server = xmlrpc.client.Server('XXX')
print(server.login(b'bHVjaGVudWU=',b'bHVjaGVudWU='))