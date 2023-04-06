
import enum


class MyInt(int):
    def __new__(cls, value):
        return super().__new__(cls, value)

class HexMixin:
    def __repr__(self):
        return hex(self)

class MyIntEnum(HexMixin, MyInt, enum.Enum):
    pass


class Foo(MyIntEnum):
    TEST = 1

assert isinstance(Foo.TEST, MyInt)
assert repr(Foo.TEST) == "0x1"
