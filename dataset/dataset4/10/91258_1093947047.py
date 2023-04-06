import binascii
import os
import socket

with socket.socket(socket.AF_ALG, socket.SOCK_SEQPACKET, 0) as cfgsock:
    cfgsock.bind(("hash", "sha256"))
    opsock, _ = cfgsock.accept()
    with opsock:
        with open("/etc/os-release") as f:
            st = os.fstat(f.fileno())
            # blindly assumes that sendfile() exhausts the fd.
            os.sendfile(
                opsock.fileno(), f.fileno(), offset=0, count=st.st_size
            )
            res = opsock.recv(512)
        print(binascii.hexlify(res))