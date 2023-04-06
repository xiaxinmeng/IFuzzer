from urllib.request import urlopen
url = 'http://localhost/u/½ñ.html'
urlopen(url.encode('utf-8')).read()