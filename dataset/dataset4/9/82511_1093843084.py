import httplib
http = httplib.HTTPSConnection('google.com')
http.request("POST", '/', None, {'Content-Type': 'text/plain',
                                 'Transfer-Encoding': 'chunked'})