# -*- encoding: utf-8 -*-
import urllib2

request = urllib2.Request('http://google.com', u'Контент', {'Content-Type': 'text/plain; charset=utf-8'})
urllib2.urlopen(request).read()