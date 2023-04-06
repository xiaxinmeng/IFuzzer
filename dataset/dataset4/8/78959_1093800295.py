
# column-major 3x2 array of bytes that was serialized
b = bytearray([1,2,3,4,5,6])

mv = memoryview(b)
mv_b = mv.cast('b', shape=(3,2))
