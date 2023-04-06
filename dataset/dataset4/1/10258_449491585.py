import SimpleHTTPServer
import logging

class MyHTTPRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.cookieHeader = self.headers.get('Cookie')
        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

    def end_headers(self):
        self.send_my_headers()
        SimpleHTTPServer.SimpleHTTPRequestHandler.end_headers(self)

    def send_my_headers(self):
        self.send_header('Set-Cookie', 'A=LDJDSFLKSDJLDSF')

if __name__ == '__main__':
    SimpleHTTPServer.test(HandlerClass=MyHTTPRequestHandler)
