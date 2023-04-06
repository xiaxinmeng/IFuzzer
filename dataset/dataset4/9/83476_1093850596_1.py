class access_rights_handler_args(ctypes.Structure):
    "access rights arguments"
    _fields_ = [('chid', ctypes.c_long),
                ('read_access', ctypes.c_uint, 1),
                ('write_access', ctypes.c_uint, 1)]