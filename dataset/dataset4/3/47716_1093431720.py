import httplib 
import urllib2

key_file = None
cert_file = None

class HTTPSClientAuthConnection(httplib.HTTPSConnection):
    def __init__(self, host):
        httplib.HTTPSConnection.__init__(self, host, key_file=key_file,
cert_file=cert_file)

class HTTPSClientAuthHandler(urllib2.HTTPSHandler):
    def https_open(self, req):
        return self.do_open(HTTPSClientAuthConnection, req)