import urllib

urlobj = urllib.urlopen("someurl")
header = urlobj.read(1)
# some other operations (no other urlobj.read())

contents = header + urlobj.read()