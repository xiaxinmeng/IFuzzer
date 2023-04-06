from unittest.mock import call, ANY, Mock

class Foo:

    def __eq__(self, other):
        pass

m = Mock(spec=Foo)
obj = Foo()
m(obj, 1)
m.assert_called_with(ANY, 1)
m.assert_any_call(ANY, 1)