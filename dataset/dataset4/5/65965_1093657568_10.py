class FixedCGIHTTPRequestHandler(CGIHTTPServer.CGIHTTPRequestHandler):
    def is_cgi(self):
        self.path = urllib.unquote(self.path)
        return CGIHTTPServer.CGIHTTPRequestHandler.is_cgi(self)