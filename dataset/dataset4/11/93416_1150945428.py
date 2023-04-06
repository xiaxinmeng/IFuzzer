#!/usr/bin/env python3

from wsgiref.simple_server import make_server
from wsgiref.validate import validator

def wsgi_callable(environ, start_response):
	body = b"this is no content at all whatsoever, I swear"
	start_response('204 No Content', [('Content-Length', str(len(body)))])
	return [body]

make_server(host='localhost', port=8080, app=validator(wsgi_callable)).serve_forever()