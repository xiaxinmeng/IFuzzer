import urllib2
url = 'http://wm.exchanger.ru/asp/XMLWMList.asp?exchtype=1'
t = urllib2.urlopen(url).read()