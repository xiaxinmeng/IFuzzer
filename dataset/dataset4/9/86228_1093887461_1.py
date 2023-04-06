
import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
data1 = r1.read()

conn.request("GET", "/")
r1 = conn.getresponse()
while chunk := r1.read(200):
    print(repr(chunk))
r1.geturl()
r1.url
