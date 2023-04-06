import os, socket, sys, time

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind('test.sock')

sock.listen(backlog=0)

while True:
    print('.', end='', file=sys.stderr)
    time.sleep(1)