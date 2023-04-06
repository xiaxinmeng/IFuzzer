from http.client import HTTPConnection

c = HTTPConnection('localhost', 8080)
c.request('GET', '/')
r = c.getresponse()

print("Status: {} {}".format(r.status, r.reason))
print("Headers: {}".format(r.getheaders()))
print("Body: {}".format(r.read()))