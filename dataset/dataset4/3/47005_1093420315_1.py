request = urllib2.Request('http://www.somesite.com/')
request.add_header('Content-Type', 'application/xml')
request.add_data(data)