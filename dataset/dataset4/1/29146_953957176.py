class X:
 x = 1

for _ in range(20):
 X.x
 print(_testcapi.type_get_version(X))
 X.x = None