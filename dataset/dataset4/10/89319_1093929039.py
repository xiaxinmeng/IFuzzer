from unittest import mock
class Foo:
  foo = 0
foo = mock.create_autospec(Foo)
mock.seal(foo)