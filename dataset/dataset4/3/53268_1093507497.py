def application(environ, start_response):
	start_response('200 OK',[('Content-type','text/html')])
	return ['<html><body>Hello World!</body></html>']
	
from wsgiref.handlers import CGIHandler
CGIHandler().run(application)