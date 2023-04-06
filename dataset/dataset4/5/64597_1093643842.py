import urllib.request
from stem import Signal
from stem.control import Controller

with Controller.from_port(port=9151) as controller:
  controller.signal(Signal.NEWNYM)

for nn in range(1, 3):
  print("case %02d" % nn)
  proxy_support = urllib.request.ProxyHandler({"socks5" : "127.0.0.1:9150"})
  opener = urllib.request.build_opener(proxy_support)
  urllib.request.install_opener(opener)
  print(urllib.request.urlopen("http://www.ifconfig.me/ip").read())