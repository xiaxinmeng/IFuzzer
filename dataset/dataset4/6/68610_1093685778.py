import base64
ascii = base64.b64encode(u"YAU-interview-revised20120921".encode(), b'-_')
print(ascii)