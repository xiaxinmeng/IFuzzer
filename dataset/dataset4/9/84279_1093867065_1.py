class M(type):
    def mro(cls):
        if cls.__name__ == 'A':
            return cls, B
        return cls,

class B(metaclass=M):
    x = 1

class A(metaclass=M):
    pass