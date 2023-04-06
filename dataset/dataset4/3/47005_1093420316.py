request = urllib2.Request('http://www.whompbox.com/headertest.php')
request.add_data(data)
f = urllib2.urlopen(request)

request.add_header('Content-Type', 'application/xml')
f = urllib2.urlopen(request)