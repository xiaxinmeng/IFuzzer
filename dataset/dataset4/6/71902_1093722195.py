import inspect
from unittest import mock

class Foo:

    def __call__(self, x):
        return x

    def bar(self, x):
        pass

m = mock.create_autospec(Foo, instance=True)
m(7)
m.bar(7)
print(inspect.signature(m))
print(m._spec_signature)
print(inspect.signature(m.bar))
print(m.bar._spec_signature)
m.bar.assert_called_once_with(7) # 7 passed as self with no value for x
m.assert_called_once_with(7) # Fails due to self