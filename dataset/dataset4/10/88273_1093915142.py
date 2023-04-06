# HTTP Server
from http.server import HTTPServer, SimpleHTTPRequestHandler  
 
port = 80  

httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
print("Starting simple_httpd on port: " + str(httpd.server_port))  
httpd.serve_forever()