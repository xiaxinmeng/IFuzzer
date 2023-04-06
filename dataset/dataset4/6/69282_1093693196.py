with support.captured_stderr() as err:
    self.con.request('GET', '/')
    res = self.con.getresponse()
    res.close()  # Not needed but cleans up socket if no Content-Length
self.con.close()  # Needed to shut down connection with Content-Length