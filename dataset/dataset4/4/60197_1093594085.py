import array
a = array.array('Q', [1])
m = memoryview(a)
m[0] = 1