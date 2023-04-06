cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor())
urllib.request.install_opener(opener)
request = urllib.request.Request(url, data, headers) # url is https://something
sock = urllib.request.urlopen(request, cafile = 'cacert.pem')