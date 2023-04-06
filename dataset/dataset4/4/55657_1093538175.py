ph = urllib.request.ProxyHandler(dict(https="proxy.example.com:3128"))
o.add_handler(ph)