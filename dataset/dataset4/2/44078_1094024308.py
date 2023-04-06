import urllib2

h = urllib2.HTTPHandler(debuglevel=1)
h2 = urllib2.HTTPSHandler(debuglevel=1)

opener = urllib2.build_opener(h)
opener2 = urllib2.build_opener(h2)
urllib2.install_opener(opener)
urllib2.install_opener(opener2)

request = urllib2.Request(url="http://www.macupdate.com/download/26915/ScreenFlow-4.5.1.dmg")
request.add_header( "User-Agent", "foo" )

url_handle = urllib2.urlopen(request)