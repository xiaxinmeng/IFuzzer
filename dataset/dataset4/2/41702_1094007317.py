from BaseHTTPServer import *

class NullHandler (BaseHTTPRequestHandler):
    def do_GET (self):
        self.send_response (100)
        self.end_headers ()

server = HTTPServer (('', 8000), NullHandler)
server.handle_request()