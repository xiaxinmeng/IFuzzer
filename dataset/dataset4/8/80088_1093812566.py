import urllib.request
req = urllib.request.Request('file:///etc/passwd')
print(f"URL scheme: {req.type}")
fp = urllib.request.urlopen(req)
print(fp.read()[:30])
fp.close()