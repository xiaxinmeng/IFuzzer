class A:
    __slots__ = ('a', )
    # fields

class B(A):
    __slots__ = ('a', 'b')
    # fields