from unittest import mock

def foo(lish):
    pass

mock_foo = mock.Mock(spec=foo)
mock_foo(1, 2)