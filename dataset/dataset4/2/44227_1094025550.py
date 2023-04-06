import urllib2
h = urllib2.HTTPHandler(debuglevel = 1)
opener = urllib2.build_opener(h)

request = urllib2.Request('http://www.google.de/')
request.header_items()

opener.open(request)
request.header_items()

request.add_header('User-agent', 'Buggy')
request.header_items()

opener.open(request)