base64string = base64.encodestring('%s:%s' %(username,passwd))[:-1]
request.add_header("Authorization","Basic %s" % base64string)
urllib2.urlopen(request)