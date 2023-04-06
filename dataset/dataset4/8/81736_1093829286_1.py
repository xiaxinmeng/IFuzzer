from unittest.mock import Mock, call, ANY

class Foo(object):
     def __eq__(self, other):
          if not isinstance(other, self.__class__):
               return NotImplemented
          return True
     def __ne__(self, other): pass

mock = Mock(spec_set=Foo)
expected = [call(ANY)]
mock(Foo())

mock.assert_has_calls(expected)