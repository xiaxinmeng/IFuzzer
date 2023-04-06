class PyTest(TestCase):
    ...
class CTest(TestCase):
    ...

class TestSomething:
    def test_something(self): ...

class TestPySomething(TestSomething, PyTest): pass
class TestCSomething(TestSomething, CTest): pass