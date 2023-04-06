class M(type):
    x = 1

class A(metaclass=M):
    pass