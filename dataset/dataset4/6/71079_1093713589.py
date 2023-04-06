import sys
try:
    import urllib.request as urllib_request
except:
    import urllib2 as urllib_request

print(sys.version)

handler = urllib_request.HTTPSHandler(debuglevel=1)
opener = urllib_request.build_opener(handler)
print(opener.open('https://httpbin.org/user-agent').read().decode('utf-8'))