proxy = ServerProxy([url])
# pre-connect timeout
proxy.transport.connection.timeout = 2
proxy.system.listMethods()