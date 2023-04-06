with support.captured_stderr() as err:
    self.con.request('GET', '/')
    res = self.con.getresponse()
    
    # Shut down connection to stop the server reading from it
    res.close()
    self.con.close()