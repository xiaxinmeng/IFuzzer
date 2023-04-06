from socket import socket, AF_ALG, SOCK_SEQPACKET, SOL_ALG, ALG_SET_KEY
from binascii import hexlify
with socket(AF_ALG, SOCK_SEQPACKET, 0) as alg:
    alg.bind(('hash', 'hmac(sha512)'))
    alg.setsockopt(SOL_ALG, ALG_SET_KEY, b'key')
    op, _ = alg.accept()
    with open('/etc/passwd', 'rb') as f:
        op.sendfile(f)
    print(hexlify(op.recv(64)))
    op.close()