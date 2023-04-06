class MyStruct(Structure):
    _fields_ = [("a", c_char), ("b", c_char), ("c", c_char)]