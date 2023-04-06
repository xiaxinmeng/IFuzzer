import urllib.request

with urllib.request.urlopen('http://www.python.org') as req:
    res = req.read()