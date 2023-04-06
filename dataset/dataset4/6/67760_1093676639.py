class MetaA(type):
    def __len__(self):
        return 0

class A(metaclass=MetaA):
    pass

class AA(A):
    pass