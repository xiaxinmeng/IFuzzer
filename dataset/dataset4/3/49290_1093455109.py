s = xmlrpc.client.ServerProxy('http://localhost/cgi-bin/rpc.py')
print(s.system.listMethods())