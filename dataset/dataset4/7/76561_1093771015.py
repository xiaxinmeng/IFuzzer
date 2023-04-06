from functools import singledispatch

class Dispatch:
    @singledispatch
    def foo(self, a):
        return a

    @foo.register(int)
    def _(self, a):
        return "int"

    @foo.register(str)
    def _(self, a):
        return "str"

cls = Dispatch()
cls.foo(3)  # 3
cls.foo('hm')  # 'hm'