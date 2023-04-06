proxy_handler = urllib2.ProxyHandler()
opener = urllib2.build_opener(proxy_handler)
urllib2.install_opener(opener)