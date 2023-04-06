import urllib.request
url = "http://www.libon.it/libon/search/isbn/3499155443"
req = urllib.request.Request(url)
response = urllib.request.urlopen(req, timeout=30)
the_page = response.read().decode('utf-8')
print(the_page)