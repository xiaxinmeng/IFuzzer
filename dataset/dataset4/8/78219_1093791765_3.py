import urllib.request
import socket
import socks

url = 'http://icanhazip.com'
socks.set_default_proxy(socks.SOCKS5, "localhost",port=8888)
socket.socket = socks.socksocket
print(urllib.request.urlopen(url).read())