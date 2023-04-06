
import http.server


class CustomRequestHandler(http.server.SimpleHTTPRequestHandler):
    protocol_version = "HTTP/1.1"


with http.server.HTTPServer(("", 8000), CustomRequestHandler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nKeyboard interrupt received, exiting.")
