class MyStructure(Structure):
    _pack_      = 1
    _fields_    = [ 
                      ("P",       c_uint16),    # 2 Bytes
                      ("L",       c_uint16, 9),
                      ("Pro",     c_uint16, 1),
                      ("G",       c_uint16, 1),
                      ("IB",      c_uint16, 1),
                      ("IR",      c_uint16, 1),
                      ("R",       c_uint16, 3), # 4 Bytes
                      ("T",       c_uint32, 10),
                      ("C",       c_uint32, 20),
                      ("R2",      c_uint32, 2)  # 8 Bytes
                  ]