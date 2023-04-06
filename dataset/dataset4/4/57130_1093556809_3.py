import http.server
import traceback

class httphandler(http.server.BaseHTTPRequestHandler):
  def do_GET(self):
    try:
      assert(False)
    except:
      self.send_error(500)

if __name__=='__main__':
  addr=('',9000)
  http.server.HTTPServer(addr,httphandler).serve_forever()