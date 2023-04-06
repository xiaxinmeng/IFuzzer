#! /usr/bin/python
import urllib2

MyHTTPPasswordMgr = urllib2.HTTPPasswordMgr
proxy = urllib2.ProxyHandler({'http': 'http://proxybiblio2.si.unimib.it:8080'})
auth = urllib2.ProxyDigestAuthHandler(MyHTTPPasswordMgr())
auth.add_password(None, "proxybiblio2.si.unimib.it", "a", "b" )
opener = urllib2.build_opener(proxy, auth, urllib2.HTTPHandler)
urllib2.install_opener(opener)
conn = urllib2.urlopen('http://webofknowledge.com')