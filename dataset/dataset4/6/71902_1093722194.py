
from unittest import mock

class Foo(object):
    def __call__(self, x):
        return x

m = mock.create_autospec(Foo, instance=True)
m(7)
m.assert_called_once_with(7)
