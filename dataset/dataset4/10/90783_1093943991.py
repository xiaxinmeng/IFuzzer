import socket
from time import monotonic

print(socket.getdefaulttimeout())
start = monotonic()
try:
    socket.create_connection(("1.1.1.1", 21), 300)
except Exception as exception:
    print(exception)