import marshal
t = [],
t[0].append(t)
b = marshal.dumps(t)
b = bytearray(b)
b[2] = b'<'[0]
marshal.loads(b)
