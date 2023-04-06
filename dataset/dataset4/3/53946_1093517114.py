x = bytearray(b'abc')
y = memoryview(x)
del y[0:1]