class X(Structure):
    _fields_ = [("a", c_short, 4),
                ("b", c_short, 4),
                ("c", c_int, 24),
                ("d", c_short, 4),
                ("e", c_short, 4),
                ("f", c_int, 24)]