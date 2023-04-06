def do_POST(self):
   # receive user-supplied data from a POST’ed HTTP request
   form_input = parse.unquote_plus(
           self.rfile.read(int(self.headers.get('content-length'))).decode('utf8')
       ).split('=')
   username = form_input[1] # extract a user-supplied value
   self.send_header('Set-Cookie', 'user={}'.format(username)) # use that value, assuming library will provide safety!
   self.end_headers()
   # ... send HTTP response body ...