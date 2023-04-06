import os, urllib.request
data = b"""{"imp": [{"h": 50, "battr": ["9", "10", "12"], "api": 3, "w": 320,
"instl": 0, "impid": "5d6dedf3-17bb-11e2-b5c0-1040f38b83e0"}]""" * 10
req = urllib.request.Request("http://localhost:8000/bogus?src=1", data)
resp = urllib.request.urlopen(req)
v = resp.read()
resp.close()
os.system("ls -alh /proc/%d/fd/*" % os.getpid())