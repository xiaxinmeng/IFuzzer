
class A:
    pass

class B:
    @property
    def __bases__(self):
        return (A(), )

print(issubclass(B(), int))
