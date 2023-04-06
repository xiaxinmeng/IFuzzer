class B:
    y = 2

class A:
    x = 1
    @property
    def __class__(self):
        return B