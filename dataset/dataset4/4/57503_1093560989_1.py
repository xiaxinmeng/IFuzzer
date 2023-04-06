# CODE
def run(server_class=http.server.HTTPServer, server_handler=http.server.SimpleHTTPRequestHandler):
    server_address = ('', PORT)
    httpd = server_class(server_address, server_handler)
    httpd.serve_forever()

class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        pass
    
if __name__ == '__main__':
    chdir(ROOTPATH)
    print("server started on PORT: "+str(PORT))
    run(server_handler=MyRequestHandler)