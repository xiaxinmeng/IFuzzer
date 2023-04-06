import ctypes
class BadStruct(ctypes.Structure):
    def __dict__(self):
        pass