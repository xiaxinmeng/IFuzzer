from socket import socket
from threading import Thread
from http.client import HTTPConnection

def serve():
    [client, _] = server.accept()
    with client, client.makefile("rb") as reader:
        while reader.readline().rstrip(b"\r\n"):
            pass
        client.sendall(
            b"HTTP/1.1 200 OK\r\n"
            b"Content-Length: 0\r\n"
            b"Extra-Space : invalid\r\n"
            b"Set-Cookie: name=value\r\n"
            b"\r\n"
        )

with socket() as server:
    server.bind(("localhost", 0))
    server.listen()
    background = Thread(target=serve)
    background.start()
    http = HTTPConnection(*server.getsockname())
    http.request("GET", "/")
    response = http.getresponse()
    print(response.msg.items())  # Set-Cookie is missing
    http.close()
    background.join()