import BaseHTTPServer, SimpleHTTPServer

server_class=BaseHTTPServer.HTTPServer
handler_class=SimpleHTTPServer.SimpleHTTPRequestHandler
server_address = ('name_of_localhost', 8080)
httpd = server_class(server_address, handler_class)
httpd.serve_forever()