def getdata(): 
    params = urllib.urlencode({'username': 'test',
'password': 'test'})
    h = httplib.HTTPS(host = "test.site.com", port =
443, key_file = "fake.pem", cert_file = "fake.pem")
    h.putrequest('POST', '/scripts/cgi.exe?')
    h.putheader('Content-length', '%d'%len(params))
    h.putheader('Accept', 'text/plain')
    h.putheader('Host', 'test.site.com')
    h.endheaders()
    h.send(params)
    reply, msg, hdrs = h.getreply()
    data = h.getfile().read()
    file('test.file', 'w').write(data)
    h.close()