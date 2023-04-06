import uuid

b = uuid.uuid1().bytes
ba = bytearray(b)
print(uuid.UUID(bytes=b))

# another API that works similarly, accepts a bytearray
print(int.from_bytes(ba, byteorder='big'))

# fails on assertion
print(uuid.UUID(bytes=ba))