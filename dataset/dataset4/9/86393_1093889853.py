class Foo:
    def __init__(self, a=set()):
        self.a = a
foo1 = Foo()
foo2 = Foo()
foo1.a.add(1)
print(foo2.a)