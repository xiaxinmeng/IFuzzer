import io
b=b"XXXX"
m=memoryview(b)
i=io.BytesIO(b'ZZZZ')
i.readinto(m)
print(b)
print(b == b"XXXX")