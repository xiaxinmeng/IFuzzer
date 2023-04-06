class Foo:
    # Compare based on attributes x, y and z
    __key__ = PyInstanceMethod_New(operator.attrgetter('x', 'y', 'z'))
    def __eq__(self, other):
        if not isinstance(other, Foo):
            return NotImplemented
        return self.__key__() == other.__key__()
    def __hash__(self):
        return hash(self.__key__())