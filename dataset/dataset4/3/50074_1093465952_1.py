#!/usr/bin/env python
import socket
USOCK = "/var/tmp/pong"
if __name__ == '__main__':
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
    sock.sendto("Ping", USOCK)