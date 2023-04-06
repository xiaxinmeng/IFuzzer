import array, ctypes
a1 = array.array('l')
a1.fromlist(range(10))
ctypes.Array.from_buffer(a1)
