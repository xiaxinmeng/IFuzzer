class A(object):
    def __radd__(self, other):
        return '__radd__', other