proxy_url = 'http://' + proxy_user + ':' + proxy_password + '@' + PROXY_IP

proxy_support = urllib2.ProxyHandler({"http":proxy_url})
opener = urllib2.build_opener(proxy_support,urllib2.HTTPHandler)
urllib2.install_opener(opener)