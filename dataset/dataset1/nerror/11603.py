class Foo(object):
    pass

Foo.__repr__ = Foo.__str__

foo = Foo()
print(str(foo))
