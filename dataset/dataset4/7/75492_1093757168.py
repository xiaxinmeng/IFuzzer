import ctypes
class BadStruct(ctypes.Structure):
    @property
    def __dict__(self):
        raise AttributeError