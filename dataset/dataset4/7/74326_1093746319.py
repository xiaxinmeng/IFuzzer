class A:
   def __init__(self, value):
       self.value = value
   def __add__(self, other):
       if not isinstance(other, A):
           return NotImplemented
       return type(self)(self.value + other.value)
   __radd__ = __add__
   def __repr__(self):
       return f'{type(self).__name__}({self.value!r})'

class B(A):
    pass

class C(A):
   def __add__(self, other):
       if not isinstance(other, A):
           return NotImplemented
       return type(self)(self.value + other.value)
   __radd__ = __add__