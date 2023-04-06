import urllib.request
request = urllib.request.Request('http://127.0.0.1:1338')
response = urllib.request.urlopen(req, timeout=1)