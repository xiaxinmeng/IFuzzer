m = memoryview(b"123")
ptr = m.buf
del m
my_ctypes_func(ptr)