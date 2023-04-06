import http.server
import traceback

class httphandler(http.server.BaseHTTPRequestHandler):
  def content_aware_error_message_format(self,m):
    oldfmt='<p>Message: %(message)s.\n'
    if oldfmt in self.error_message_format:
      # use <pre> if the message contains a newline internally
      # otherwise let the html control line breaks
      self.error_message_format=self.error_message_format.replace(oldfmt,'<p><pre>%(message)s</pre>\n') if '\n' in m else self.error_message_format.replace(oldfmt,'<p>%(message)s\n')
  def do_GET(self):
    try:
      assert(False)
    except:
      m=traceback.format_exc().strip()
      self.content_aware_error_message_format(m)
      self.send_error(500,m)

if __name__=='__main__':
  addr=('',9000)
  http.server.HTTPServer(addr,httphandler).serve_forever()