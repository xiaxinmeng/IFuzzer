__obj = object()

class Foo:
    def f1(self):
        nonlocal __obj

f = Foo()
f.f1()
