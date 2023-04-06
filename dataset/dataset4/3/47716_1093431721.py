import httplib 
import urllib2

key_file = 'mykey.pem'
cert_file = 'mycert-signed.pem'

class HTTPSClientAuthConnection(httplib.HTTPSConnection):
    def __init__(self, host, timeout=None):
        httplib.HTTPSConnection.__init__(self, host, key_file=key_file,
cert_file=cert_file)
        self.timeout = timeout # Only valid in Python 2.6

class HTTPSClientAuthHandler(urllib2.HTTPSHandler):
    def https_open(self, req):
        return self.do_open(HTTPSClientAuthConnection, req)