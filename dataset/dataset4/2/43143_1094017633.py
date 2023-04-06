import urllib2
proxy_handler = urllib2.ProxyHandler({"http":
"localhost:3128"})
urllib2.build_opener(proxy_handler).open('http://python.org/')