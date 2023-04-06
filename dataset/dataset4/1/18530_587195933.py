
class A:
    @property
    def __bases__(self):
        return (int, )


class B:
    @property
    def __bases__(self):
        return (A(), )


assert issubclass(B(), int)
