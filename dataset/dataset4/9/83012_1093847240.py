import urllib.request
header = {"Test-Header":"Value"}
requestobject = urllib.request.Request("https://www.example.com",None,header)
print ("Original header is:", header)
print ("Request header is:", requestobject.header_items())