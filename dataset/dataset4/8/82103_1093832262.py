
import inspect


def foo0():
    class Foo:
        x = 4
    return Foo


def foo1():
    class Foo:
        x = 5
    return Foo


print(inspect.getsource(foo1()))

print(foo1().x)
print(foo0().x)
