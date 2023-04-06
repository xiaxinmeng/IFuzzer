#!/usr/bin/env python3
import socket
import ssl

hostname = '145.100.57.105.surf-hosted.nl'
# hostname = 'python.org'

context = ssl.create_default_context()

with socket.create_connection((hostname, 443)) as sock:
    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
        cert = ssock.getpeercert()
        print(cert)