#!/usr/bin/env python3.3
import http.server


class HTTPHandler(http.server.BaseHTTPRequestHandler):
    "A very simple server"
    def do_GET(self):
        self.send_response('foobar')
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(bytes('Response body\n\n', 'latin1'))

if __name__ == '__main__':
    addr = ('', 9000)
    http.server.HTTPServer(addr, HTTPHandler).serve_forever()