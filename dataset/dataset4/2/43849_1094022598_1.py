import httplib
...
class HTTPResponse(httplib.HTTPResponse):
    def __init__(self, sock, **kw):
        httplib.HTTPResponse.__init__(self, sock, **kw)
        self.fp = sock.makefile('rb') 

httplib.HTTPConnection.response_class = HTTPResponse