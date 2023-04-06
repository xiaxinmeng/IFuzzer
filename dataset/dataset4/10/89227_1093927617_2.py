class B:
    def __init__(self, f):
        self.f = f

    def __get__(self, obj, objtype=None):
        raise NameError("Python bug?")