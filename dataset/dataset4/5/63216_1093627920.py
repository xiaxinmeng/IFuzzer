import mock
from collections import namedtuple

Foo = namedtuple('Foo', bar)
mock_foo = mock.create_autospec(Foo)

if mock_foo:
    print('the namedtuple is truthy')
else:
    print('the namedtuple is not truthy')