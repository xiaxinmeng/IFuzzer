def c_array(*args):
    if type(args[1]) is int:
        ptr, size = args
        return (ptr._type_ * size).from_address(ct.addressof(ptr.contents))
    else:
        c_type, buf = args
        return (c_type * (len(buf) // ct.sizeof(c_type))).from_buffer_copy(buf)