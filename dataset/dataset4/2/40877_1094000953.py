class dylib_reference(Structure):
    _fields_ = (
        # XXX - ick, fix
        ('isym_flags', p_ulong),
        #('isym', p_ubyte * 3),
        #('flags', p_ubyte),
    )