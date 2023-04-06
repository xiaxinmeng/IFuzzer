class C(A, B, metaclass=meta):
    def f(self):
        return __class__