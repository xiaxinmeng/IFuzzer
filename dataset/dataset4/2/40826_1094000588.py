# from urllib2 import ...
proxy = {"http":"http://user:pwd@proxy:port"}
opener =build_opener(ProxyHandler(proxy))
install_opener( opener )

req = Request(coolurl)
# construct 
base64string = base64.encodestring('%s:%s' % (site_user,
site_pwd))[:-1]
authheader =  "Basic %s" % base64string
req.add_header("Authorization", authheader)
urlopen( req )