import urllib
req = urllib.urlopen('file:///etc/passwd')
print(req.read()[:30])
req.close()