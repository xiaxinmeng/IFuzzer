form = cgi.FieldStorage(fp=self.rfile,
                        headers=self.headers,
                        environ={"REQUEST_METHOD":op.upper(),
                              "CONTENT_TYPE":self.headers['Content-Type'],})