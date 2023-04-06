from socket import socket, AF_INET, SOCK_STREAM
from ssl import wrap_socket, PROTOCOL_TLSv1, CERT_NONE

def test_handshake(address, WORKAROUND):

    s = socket(AF_INET, SOCK_STREAM)
    s.settimeout(3.0)
    s.connect(address)

    if WORKAROUND:
        s.getpeername()

    ssl = wrap_socket(s, server_side = False,
                      ssl_version = PROTOCOL_TLSv1,
                      cert_reqs = CERT_NONE,
                      do_handshake_on_connect = False)
    ssl.do_handshake()

address = ("www.amazon.com", 443)

test_handshake(address, True) # with workaround
print("worked so far")
test_handshake(address, False)
print("but not here it didn't")