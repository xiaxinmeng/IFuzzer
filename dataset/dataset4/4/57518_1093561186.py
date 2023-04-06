t = time.gmtime(time.time())
s = time.strftime('%Z', t)
print(s)

time.mktime((-1, 1, 1, 0, 0, 0, -1, -1, -1))
s = time.strftime('%Z', t)
print(s)

time.mktime((1, 1, 1, 0, 0, 0, 0, 0, -1))
s = time.strftime('%Z', t)
print(s)