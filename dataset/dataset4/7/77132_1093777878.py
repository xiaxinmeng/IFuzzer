import socket
import ssl

cafile = ssl.get_default_verify_paths().cafile

with socket.socket() as sock:
    ssock = ssl.SSLSocket(
        sock,
        cert_reqs=ssl.CERT_REQUIRED,
        ca_certs=cafile,
        server_hostname='www.python.org'
    )
    ssock.connect(('www.evil.com', 443))