# Before:
proxies['https'] = 'https://%s' % proxyServer

# After:
proxies['https'] = 'http://%s' % proxyServer