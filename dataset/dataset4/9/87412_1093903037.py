
class Parent:
    def __init__(self, value):
        self._value = value

    def method(self):
        return self._value


class Child1(Parent):
    pass


c1 = Child1(42)
result = c1.method()
assert result == 42, result


class Child2(Parent):
    def method(self):
        return super().method()


c2 = Child2(42)
result = c2.method()
assert result == 42, result
