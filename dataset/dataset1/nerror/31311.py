import ctypes
class BadStruct(ctypes.Structure):
    def __dict__(self):
        pass

BadStruct().__setstate__({}, b'foo')
