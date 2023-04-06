class HTTPConnection:

    def getresponse(self):
            response = self.response_class(self.sock, ...)
            ...
            if response.will_close:
                # this effectively passes the connection to the response
                self.close()

    def close(self):
        if self.sock:
            self.sock.close()
        ...

class HTTPResponse:
    def __init__(self, sock, debuglevel=0, strict=0, method=None):
        self.fp = sock.makefile('rb', 0)
        ...