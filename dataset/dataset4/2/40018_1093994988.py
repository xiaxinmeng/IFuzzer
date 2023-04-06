from urllib2 import *
req = Request("http://someurl/page.html",
headers={'range: bytes=%s':'20-40'})
result = urlopen(req)