class C:
    def prop(self, function):
        return property(function)

class F:
    @C().prop
    def foo(self):
        return 5