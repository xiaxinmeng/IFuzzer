import httplib

host = 'proxy.corp.com:8181'  # this is not the actual proxy

selector = 'https://www.python.org'

print("Trying to open", selector)

h = httplib.HTTP(host)
h.putrequest('GET', selector)
h.putheader('User-Agent', 'Python-urllib/1.17')
h.endheaders(None)
errcode, errmsg, headers = h.getreply()

print(errcode, errmsg)
print(headers.items())