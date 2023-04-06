import urllib2, urllib, time
import cookielib
            
req_url = 'http://google.com'

## OPEN COOKIE JAR - Optional
cj = cookielib.CookieJar()

cookie_handler = urllib2.HTTPCookieProcessor(cj)
opener = urllib2.build_opener(cookie_handler)
urllib2.install_opener(opener)

req = urllib2.Request(url=req_url)
    
cj.add_cookie(req, 'cname2', 'cval2',
                {'expires':  int(time.time()) + 3600,})

cj.add_cookie(req, 'cname3', 'cval3') 