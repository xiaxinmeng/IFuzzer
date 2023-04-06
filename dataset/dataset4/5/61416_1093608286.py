import urllib.request
from urllib.parse import quote
url = "http://www.libon.it/libon/search/isbn/3499155443"
req = urllib.request.Request(url)
req.selector = urllib.parse.quote(req.selector)
response = urllib.request.urlopen(req, timeout=30)
the_page = response.read().decode('utf-8')
print(the_page)