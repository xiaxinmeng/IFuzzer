import urllib
with urllib.request.urlopen('http://www.py4inf.com/code/romeo.txt') as f:
    print(f.read())