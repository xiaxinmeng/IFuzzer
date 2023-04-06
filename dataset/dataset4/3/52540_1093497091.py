import httplib

http_connection = httplib.HTTPConnection("192.168.192.196")
http_connection.request("GET", "/")
http_connection.sock.settimeout(20)
response = http_connection.getresponse()
data = response.read()
http_connection.close()