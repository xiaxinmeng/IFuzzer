import ssl
print((ssl.HAS_TLSv1, ssl.HAS_TLSv1_1, ssl.HAS_TLSv1_2, ssl.HAS_TLSv1_3))
print(ssl.SSLContext().maximum_version)
print(ssl.SSLContext().minimum_version)