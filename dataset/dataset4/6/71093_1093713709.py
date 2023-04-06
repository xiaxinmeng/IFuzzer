class M(type):
    def mro(self):
        hasattr(self, 'foo')
        return type.mro(self)

class C(metaclass=M):
    pass