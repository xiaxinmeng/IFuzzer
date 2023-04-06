import httplib
params = '\n'*10
h = httplib.HTTP('localhost', 8080)
h.putrequest('POST', '/')
h.putheader('Content-type', 'multipart/form-data')
h.putheader('Content-length', str(len(params)))
h.endheaders()
h.send(params)