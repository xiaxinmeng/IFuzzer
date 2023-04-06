handler = request.HTTPSHandler(debuglevel=1)
opener = request.build_opener(handler)
f = opener.open('https://httpbin.org/user-agent')