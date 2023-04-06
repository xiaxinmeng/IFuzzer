import urllib.request as ur, http.cookiejar as ck
cookie_jar = ck.CookieJar()
request = ur.Request('http://gdyn.cnn.com/1.1/1.gif?1301540335193')
conn = ur.urlopen(request)
cookie_jar.make_cookies(conn, request)