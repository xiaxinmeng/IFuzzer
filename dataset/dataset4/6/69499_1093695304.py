from unittest.mock import call, create_autospec, Mock
import inspect

class Foo:

    def __init__(self, val):
        pass

    def func(self):
        pass

class FooMock(Mock):

    def _get_child_mock(self, **kwargs):
        return create_autospec(Foo)

mock_foo = FooMock()
print(inspect.signature(mock_foo.func)) # Signature is correct with create_autospec whereas with Mock(spec=Foo) it is (*args, **kwargs)
mock_foo.func() # Raises TypeError with (val) being signature.
mock_foo.func.assert_has_calls([call()])