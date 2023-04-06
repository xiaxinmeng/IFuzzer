import urllib.request as ur
import socket
s = socket.socket()
s.bind(('localhost', 10000))
s.listen(0)
socket.setdefaulttimeout(5)
ur.urlopen('http://localhost.localdomain:10000')