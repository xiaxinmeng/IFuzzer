import http.server

class CompressedHandler(http.server.SimpleHTTPRequestHandler):

    compressed_types = ["text/html", "text/plain"]

http.server.test(HandlerClass=CompressedHandler)