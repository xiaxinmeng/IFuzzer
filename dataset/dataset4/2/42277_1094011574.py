pwmgr=urllib2.HTTPPasswordMgrWithDefaultRealm()
pwmgr.add_password(None, url, username, password)
handler=urllib2.HTTPBasicAuthHandler(pwmgr)
opener=urllib2.build_opener(handler)
urllib2.install_opener(opener)
u=urllib2.urlopen(url)