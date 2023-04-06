import typing

def f():
    A = typing.TypeVar("A")
    def same_type_args(a: A, b: A):
        assert type(a) == type(b)
    print(typing.get_type_hints(same_type_args, localns=locals()))