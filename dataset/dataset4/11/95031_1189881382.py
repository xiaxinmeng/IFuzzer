import ssl
import sys
import time

LOOPS = 100

print(sys.version)
print(ssl.OPENSSL_VERSION)

ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)

start = time.monotonic()
for i in range(LOOPS):
    ctx.load_verify_locations('/etc/pki/tls/cert.pem')
dur = time.monotonic() - start
print(f"{LOOPS} loops of 'load_verify_locations' in {dur:0.3f}sec")