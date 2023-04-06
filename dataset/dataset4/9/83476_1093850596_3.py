class access_rights_handler_args(ctypes.Structure):
    "access rights arguments"
    _fields_ = [('chid', ctypes.c_long),
                ('access', ctypes.c_ubyte)]