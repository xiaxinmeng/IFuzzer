class A:
   __slots__ = ['a']

a = A()
a.a = ... # OK
a.b = ... # raises AttributeError

A.__slots__ = ['b']
a.a = ... # still OK
a.b = ... # still raises AttributeError