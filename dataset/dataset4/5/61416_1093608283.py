import urllib.request
from urllib.parse import quote
url = "http://www.libon.it/ricerca/7817940/3499155443/dettaglio/3102314/Onkel-Oswald-und-der-Sudan-KÃ¤fer/order/date_desc"

req = urllib.request.Request(url)
try:
    req.selector.encode('ascii')
except UnicodeEncodeError:
    req.selector = quote(req.selector)
response = urllib.request.urlopen(req, timeout=30)
the_page = response.read().decode('utf-8')
print(the_page)