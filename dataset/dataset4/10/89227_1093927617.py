class A1:
    def __getattr__(self, name):
        print("A1 visited")
        raise AttributeError(f"{self.__class__.__name__}: {name} not found.")

class A2(A1):
    def __getattr__(self, name):
        print("A2 visited")
        super().__getattr__(name)


class A3(A2):
    def __getattr__(self, name):
        print("A3 visited")
        super().__getattr__(name)


class B:
    def __init__(self, f):
        self.f = f

    def __get__(self, obj, objtype=None):
        raise AttributeError("Python bug?")

class C(A3):
    @B
    def test(self):
        return 25