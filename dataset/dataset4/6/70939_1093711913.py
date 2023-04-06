from unittest.mock import *

class Foo:

    def __init__(self, a, b):
        pass

    def foo(self, a):
        pass


mock_class = create_autospec(Foo)
mock = mock_class(1, 2)
mock.foo(1)
print(mock_class._mock_children)
print(mock._mock_children)
mock_class.assert_has_calls([call(1, 2), call().foo(1)])
mock.assert_has_calls([call.foo(1)])