
import urllib.request

req = urllib.request.Request('http://127.0.0.1:8085')
response = urllib.request.urlopen(req, timeout=1)
