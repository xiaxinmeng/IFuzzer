
class Foo:
    pass


Foo.foo = property(name='foo')

f = Foo()
f.foo = 10
