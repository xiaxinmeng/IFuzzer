import CGIHTTPServer
import BaseHTTPServer

if __name__ == "__main__":
    server = BaseHTTPServer.HTTPServer
    handler = CGIHTTPServer.CGIHTTPRequestHandler
    server_address = ("", 8000)
    # Note that only /cgi-bin will work:
    handler.cgi_directories = ["/cgi-bin", "/cgi-bin/subdir"]
    httpd = server(server_address, handler)
    httpd.serve_forever()