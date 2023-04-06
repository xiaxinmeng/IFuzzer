url = "http://www.python.org"

req = urllib2.Request(url)
req.add_header('Connection',"keep-alive")
u = urllib2.urlopen(req)