class Complex64(Structure):
    _fields_ = [("real", c_float), ("imag", c_float)]