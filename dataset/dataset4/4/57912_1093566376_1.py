sizeof_long = ctypes.sizeof(ctypes.c_long)
r_bits = 8
r = array.array('l', os.urandom((2**r_bits) * sizeof_long))
r_mask = 2**r_bits-1