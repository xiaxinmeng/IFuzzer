
from unittest.mock import Mock, call
class X(object):
    def __init__(self):pass
    def foo(self, a):pass
x = Mock(spec=X)
x.foo(20)
x.assert_has_calls(x.mock_calls)
