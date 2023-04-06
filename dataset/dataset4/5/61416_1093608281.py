import urllib.request
url = "http://www.libon.it/ricerca/7817940/3499155443/dettaglio/3102314/Onkel-Oswald-und-der-Sudan-KÃ¤fer/order/date_desc"

req = urllib.request.Request(url)
response = urllib.request.urlopen(req, timeout=30)
the_page = response.read().decode('utf-8')
print(the_page)