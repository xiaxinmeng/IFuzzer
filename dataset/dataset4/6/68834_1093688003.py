ctx = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
ctx.verify_mode = ssl.CERT_REQUIRED
ctx.load_verify_locations(cadata=dummy_certificate)