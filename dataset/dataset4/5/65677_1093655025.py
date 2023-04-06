import unittest.mock as mock

def foo():
    pass

parent = mock.Mock()
parent.child = mock.create_autospec(foo)
parent.child()
print(parent.mock_calls)