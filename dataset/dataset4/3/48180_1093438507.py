#!/usr/bin/env python3
import sys
import urllib.request
print(sys.version)
fh = urllib.request.urlopen("http://www.python.org/index.html")
data = fh.read()
fh.close()
print(type(data))