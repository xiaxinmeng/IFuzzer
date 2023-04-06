class D:
    def foo(self):
        return 5
    foo = C().prop(foo)

class E:
    c = C()
    @c.prop
    def foo(self):
        return 5