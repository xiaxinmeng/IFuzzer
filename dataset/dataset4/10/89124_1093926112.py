from functools import update_wrapper


class foo_deco:
    def __init__(self, func):
        self._func = func
        update_wrapper(self, func)

    def __call__(self, *args, **kwargs):
        return self._func(*args, **kwargs)


class bar_deco:
    def __init__(self, func):
        self._func = func
        update_wrapper(self, func)

    def __call__(self, *args, **kwargs):
        return self._func(*args, **kwargs)


class Foo:
    @classmethod
    @foo_deco
    def bar_cm(self):
        pass

    @bar_deco
    @foo_deco
    def bar_bar(self):
        pass


print(Foo.bar_cm.__wrapped__)
# <function Foo.bar_cm at 0x7fb0254433a0>
print(Foo.bar_bar.__wrapped__)
# <__main__.foo_deco object at 0x7fb025445fd0>

# The foo_deco object is available on bar_cm this way though
print(Foo.__dict__['bar_cm'].__func__)
# <__main__.foo_deco object at 0x7fb025445fa0>