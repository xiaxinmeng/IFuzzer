import _struct

s = _struct.Struct('i')

class C:
    def __del__(self):
        s.pack(42, 100)

_struct.x = C()