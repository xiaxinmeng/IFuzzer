x = bytearray(b'abc')
y = x.replace(b'abc', b'bar', 0)
id(x) == id(y)