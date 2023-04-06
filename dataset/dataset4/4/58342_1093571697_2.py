proxy = ServerProxy([url])
proxy.system.listMethods()
# socket is available as connection has been established
proxy.transport.connection.sock.settimeout(2)