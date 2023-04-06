cookie = http.cookiejar.CookieJar()
cookie_handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(cookie_handler)