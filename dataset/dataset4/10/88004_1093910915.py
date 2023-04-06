from types import MappingProxyType

orig = {1: 2}
proxy = MappingProxyType(orig)

class X:
    def __eq__(self, other):
        other[1] = 3