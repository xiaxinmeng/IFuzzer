base64string = base64.encodestring('%s:%s' % (username, password))[:-1]


conn = httplib.HTTPSConnection(HOSTNAME,key_file = key,cert_file = cert)
conn.putrequest('GET', '/')
conn.putheader("Authorization", "Basic %s" % base64string)

conn.endheaders()
response = conn.getresponse()