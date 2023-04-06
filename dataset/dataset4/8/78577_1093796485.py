if __name__ == '__main__':

    import timeit
    from collections import OrderedDict as FastDictSub
    from ctypes import *
    
    class mappingmethods(Structure):
        _fields_ = [
            ('mp_length', c_void_p),
            ('mp_subscript', PYFUNCTYPE(py_object,py_object,py_object)),
            ('mp_ass_subscript', c_void_p)]
        
    class _type_object(Structure):
        _fields_ = [('junk', (c_uint8*56)), # <- brevity
                    ('tp_as_mapping', POINTER(mappingmethods))]
    py_type = POINTER(_type_object)
    
    class SlowDictSub(dict):
        pass