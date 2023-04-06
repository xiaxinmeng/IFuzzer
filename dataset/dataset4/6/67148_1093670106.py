import http.client
import ssl

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
ssl_context.verify_mode = ssl.CERT_REQUIRED
ssl_context.check_hostname = False
https = http.client.HTTPSConnection("localhost", context=ssl_context)
print(https._check_hostname)