
#!/usr/bin/env python3

import socket
import ssl

HOST = 'websocket-cs.vudu.com'
PORT = 443

sock = socket.create_connection((HOST, PORT))
ctx = ssl.create_default_context()
ssock = ctx.wrap_socket(sock, server_hostname=HOST)
print("Connection successful")
