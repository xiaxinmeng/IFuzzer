class Parent:
    def foo(self, **kwargs):
        """Argument names of foo vary depending on the child class."""


class Child(Parent):
    @overload
    def foo(self, a, b):
        pass