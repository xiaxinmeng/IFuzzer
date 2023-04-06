import os
import socket

with open("/tmp/test", "wb") as fp:
    fp.write(b"testdata\n" * 1000000)

cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cli.connect(('localhost', 8010))
c = cli.fileno()
f = os.open("/tmp/test", os.O_RDONLY)

os.sendfile(c, f, 1, 7) # "estdata"
cli.send(b"\n\n")
os.sendfile(c, f, None, 4) # "test"
cli.send(b"\n\n")
os.sendfile(c, f, None, 4) # "data"
cli.send(b"\n\n")