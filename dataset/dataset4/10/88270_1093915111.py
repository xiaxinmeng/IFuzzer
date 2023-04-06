from http import cookies
C = cookies.SimpleCookie()
C["ys-api/mpegts/service"] = "blabla"
print(C.output())