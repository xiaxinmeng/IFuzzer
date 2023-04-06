import httplib
h = httplib.HTTPConnection('localhost', 8888)
h.connect()
h.request('GET', '/')
r = h.getresponse()