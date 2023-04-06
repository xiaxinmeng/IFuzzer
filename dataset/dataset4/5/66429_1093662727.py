import http.client
c = http.client.HTTPSConnection("graph.facebook.com")
c.request("GET", "/%C4%85", None, {"test": "\x85"})
r = c.getresponse()
print(r.headers)
print(r.headers.keys())
print(r.headers.get("WWW-Authenticate"))