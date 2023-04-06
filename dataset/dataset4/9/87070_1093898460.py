from typing import TypeVar, Generic
T = TypeVar('T')

class A(Generic[T]):
    __annotations__ = dict(
        some_b='B'
    )


class B(Generic[T]):
    class A(Generic[T]):
        pass
    __annotations__ = dict(
        my_inner_a1='B.A',
        my_inner_a2=A,
        my_outer_a='A'  # unless somebody calls get_type_hints with localns=B.__dict__
    )