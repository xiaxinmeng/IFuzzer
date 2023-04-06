import urllib.request
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor())
urllib.request.install_opener(opener)
request = 'https://httpbin.org/cookies/set?name=value'
# Download certifiate chain for https://httpbin.org/ into cacert.pem (I used Firefox)
sock = urllib.request.urlopen(request, cafile = 'cacert.pem')
sock.read()  # b'{\n  "cookies": {}\n}\n' (No cookies!)
sock.close()
sock = urllib.request.urlopen(request)  # Default SSL settings
sock.read()  # b'{\n  "cookies": {\n    "name": "value"\n  }\n}\n'