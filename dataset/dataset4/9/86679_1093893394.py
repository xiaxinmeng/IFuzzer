import socket
self.__socket = socket.create_connection ([host, port], 10000)
value = self.__socket.recv (4096)