def test_304():
    import time
    from email.utils import formatdate
    from wsgiref.simple_server import make_server

    def demo_app(environ, start_response):
        if 'HTTP_IF_MODIFIED_SINCE' in environ:
            start_response("304 Not Modified", [])
            return []
        headers = [('Content-Type', 'text/html; charset=utf-8'),
                   ('Last-Modified', formatdate(time.time(), usegmt=True))]
        start_response("200 OK", headers)
        return ["Hello World!"]

    httpd = make_server('127.0.0.1', 8000, demo_app)
    sa = httpd.socket.getsockname()
    print("Serving HTTP on %s port %s ..." % sa)
    httpd.serve_forever()

if __name__ == '__main__':
    test_304()