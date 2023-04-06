import typing
T = typing.TypeVar('T')

def test():
    class Nested(typing.Generic[T]):
        pass

    class Test(typing.Generic[T]):
      nested: Nested[T]

    typing.get_type_hints(Test) # this throws

test()