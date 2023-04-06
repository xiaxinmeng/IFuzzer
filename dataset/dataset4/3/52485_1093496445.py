import time
import urllib2

timeMark = time.time()
opener = urllib2.build_opener()

proxy = urllib2.ProxyHandler({"http" : "http://10.249.1.63:80"})
opener.add_handler(proxy)

textWeb = opener.open("http://www.google.com/").read()