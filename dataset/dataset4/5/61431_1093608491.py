class HTTPHandler(AbstractHTTPHandler):

    _connection = httplib.HTTPConnection
    
    @property
    def connection(self):
        """Returns the class of connection being handled."""
        return self._connection

    def http_open(self, req):
        return self.do_open(_connection, req)

    http_request = AbstractHTTPHandler.do_request_