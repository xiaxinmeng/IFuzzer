import ssl, http
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
context.set_tls_username_password('jsmith', 'abc')
h = http.client.HTTPSConnection('tls-srp.test.trustedhttp.org', 443, context=context)
h.request('GET', '/')
resp = h.getresponse()
print(resp.status)
# => 200
print(resp.read())
# => "user: jsmith"