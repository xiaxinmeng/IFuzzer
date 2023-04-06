import _struct

class C:
    def __init__(self):
        self.pack = _struct.pack
    def __del__(self):
        self.pack('I', -42)

_struct.x = C()