#!/usr/bin/python
# vim: fileencoding=utf8 
# test with:  echo | socat - tcp4-listen:1111,fork
# Demonstrates bad content length of second request, which should be 2
import urllib2
req = urllib2.Request('http://localhost:1111')
req.add_data("1")
urllib2.urlopen(req)
req.add_data("10")
urllib2.urlopen(req)