
class Parent:
    def foo(self, **kwargs):
        """Argument names of foo vary depending on the child class."""


class Child(Parent):
    def foo(self, a, b):
        super().foo(a=a, b=b)
