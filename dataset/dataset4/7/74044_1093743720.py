
import functools, inspect


def decorator(func):
    @functools.wraps(func)
    def inner(*args):
        return func(*args)
    return inner


class Foo(object):
    @decorator
    def bar(self, testarg):
        pass


f = Foo()
baz = decorator(f.bar)
assert inspect.signature(baz) == inspect.signature(f.bar)
