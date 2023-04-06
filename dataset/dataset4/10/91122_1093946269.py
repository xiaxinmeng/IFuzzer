dim = lib.get_array_size(opaque)
ptrs = (c_void_p * dim)()
lib.get_array_values(opaque, ptrs)
for ptr in ptrs:
    print(lib.get_object_value(ptr))