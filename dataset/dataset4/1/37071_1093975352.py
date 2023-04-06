import httplib
import time

for i in range(1000):
    conn = httplib.HTTPConnection("www.python.org")
    conn.request("GET", "/index.html")
    r1 = conn.getresponse()
    time.sleep(0.5)
    conn.close()