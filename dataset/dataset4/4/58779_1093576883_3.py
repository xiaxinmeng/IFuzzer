httpd = ThreadedHTTPServer(("127.0.0.1", 8000), RequestHandler)
httpd.serve_forever()
httpd.server_close()