
import typing

T = typing.TypeVar('T')
class Base(typing.Generic[T]):
    some_attribute: typing.Any

    def __init_subclass__(cls, **kwargs):
        assert hasattr(cls, 'some_attribute')

class Class1(Base):       # OK
    some_attribute = 123  

class Class2(Base[int]):  # AssertionError
    some_attribute = 123  
