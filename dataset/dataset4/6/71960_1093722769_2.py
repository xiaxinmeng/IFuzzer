import ssl, socket, _socket

s = ssl.wrap_socket(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
s.context._wrap_socket(_socket.socket(), server_side=1)