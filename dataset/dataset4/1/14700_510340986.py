from unittest.mock import call, ANY, Mock

class Foo:

    def __eq__(self, other):
        if not isinstance(other, Foo):
            return False
        return True

m = Mock()
obj = Foo()
m(obj, 1)
m.assert_has_calls([call(ANY, 1)])