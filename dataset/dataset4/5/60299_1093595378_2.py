#! /usr/bin/python
from urllib import request
MyHTTPPasswordMgr = request.HTTPPasswordMgr
proxy = request.ProxyHandler({'http': 'http://proxybiblio2.si.unimib.it:8080'})
auth = request.ProxyDigestAuthHandler(MyHTTPPasswordMgr())
auth.add_password(None, "proxybiblio2.si.unimib.it", "a", "b" )
opener = request.build_opener(proxy, auth, request.HTTPHandler)
request.install_opener(opener)
conn = request.urlopen('http://webofknowledge.com')