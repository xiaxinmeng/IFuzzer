# Python 3
from urllib.request import urlopen, build_opener
opener = build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0' + chr(0x0A) + "Location: header injection")]
opener.open("http://localhost:9999")