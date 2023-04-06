from wsgiref.simple_server import make_server, demo_app
with make_server('', 8000, demo_app) as httpd:
    print("Serving HTTP on port 8000...")
    httpd.serve_forever()