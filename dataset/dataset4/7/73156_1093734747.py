with StructMap(ctypes_struct, mm, offest) as smap:
    smap.xxx = 'blabla'
del smap # necessary, but ugly