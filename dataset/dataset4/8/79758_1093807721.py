from unittest import mock

class SomeClass:
    def do_something(self, x):
        pass

def some_function(x):
    obj = SomeClass()
    y = obj.do_something(x)
    return y

def do_something_side_effect(self, x):
    print(self)
    return x

def test_some_function():
    with mock.patch.object(SomeClass, "do_something", do_something_side_effect):
        assert some_function(1)