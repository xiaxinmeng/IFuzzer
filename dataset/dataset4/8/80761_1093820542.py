import dataclasses
import unittest.mock

@dataclasses.dataclass
class Foo:
    name: str
    baz: float
    bar: int = 12

FooMock = unittest.mock.create_autospec(Foo)
fooMock = FooMock()  # Will fail now since it's specced