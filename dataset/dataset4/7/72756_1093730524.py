import socket
import time

document = b'''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>title</title>
    <link rel="stylesheet" href="/other/styles.css">
    <script src="/other/action.js"></script>
  </head>
  <body>
    <h1>Hello, world!</h1>
  </body>
</html>
'''

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('localhost', 8080))
s.listen(5)

while True:
    new_socket, _ = s.accept()
    data = b''

    while not data.endswith(b'\r\n\r\n'):
        data += new_socket.recv(8192)

    new_socket.sendall(
        b'HTTP/1.1 103 Early Hints\r\n'
        b'Server: socketserver/1.0.0\r\n'
        b'Link: </other/styles.css>; rel=preload; as=style\r\n'
        b'Link: </other/action.js>; rel=preload; as=script\r\n'
        b'\r\n'
    )
    time.sleep(1)
    new_socket.sendall(
        b'HTTP/1.1 200 OK\r\n'
        b'Server: socketserver/1.0.0\r\n'
        b'Content-Type: text/html\r\n'
        b'Content-Length: %s\r\n'
        b'Link: </other/styles.css>; rel=preload; as=style\r\n'
        b'Link: </other/action.js>; rel=preload; as=script\r\n'
        b'Connection: close\r\n'
        b'\r\n' % len(document)
    )
    new_socket.sendall(document)
    new_socket.close()