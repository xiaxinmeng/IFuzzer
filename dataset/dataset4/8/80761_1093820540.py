import dataclasses
import unittest.mock

@dataclasses.dataclass
class Foo:
    name: str
    baz: float
    bar: int = 12

FooMock = unittest.mock.Mock(Foo)
fooMock = FooMock()  # should fail: Foo.__init__ takes two arguments
# I would expect these to be True, but they are False
'name' in dir(fooMock)
'baz' in dir(fooMock)
'bar' in dir(fooMock)