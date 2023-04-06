from http.server import HTTPServer, BaseHTTPRequestHandler

class RequestHandler(BaseHTTPRequestHandler):
	def _header(self):
		self.send_response(200)
		self.send_header("Content-type", "text/html")
		self.end_headers()
		
	def do_HEAD(self):
		self._header()
		
	def do_GET(self):
		self._header()	
		
		self.wfile.write('test')
		
server = HTTPServer(('localhost', 80), RequestHandler)
server.serve_forever()