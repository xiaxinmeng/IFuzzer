
In [1]: m = memoryview(b"abcdef")

In [2]: m2 = m.cast("B", (2, 3))
