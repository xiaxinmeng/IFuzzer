def run_while_true(keep_running,
                   server_class=BaseHTTPServer.HTTPServer,
                   handler_class=BaseHTTPServer.BaseHTTPRequestHandler):
    """keep_running is a function of no arguments which is tested initially and
    after each request. If its return value evaluates to True, the server
    continues."""
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    while keep_running:
        httpd.handle_request()