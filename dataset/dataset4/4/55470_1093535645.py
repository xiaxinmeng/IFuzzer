import urllib, urllib.request, urllib.error, urllib.parse

form = urllib.parse.urlencode({'field1':'Log in'})
try:
	response = urllib.request.urlopen('http://www.google.com/', form)
except urllib.error.HTTPError as exception:
	print (exception)