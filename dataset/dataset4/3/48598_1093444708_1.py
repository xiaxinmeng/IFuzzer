t = bytearray()
for i in range(256): t.append(i)

x = bytearray(b'')
y = x.translate(t)
id(x) == id(y)