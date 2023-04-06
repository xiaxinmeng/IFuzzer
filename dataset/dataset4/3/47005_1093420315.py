request = urllib2.Request('http://www.somesite.com/')
request.add_data(data)
f = urllib2.urlopen(request)