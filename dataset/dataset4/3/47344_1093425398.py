import httplib
conn = httplib.HTTPSConnection("my-secure-domain.com")
conn.request("GET", "/")
res = conn.getresponse()