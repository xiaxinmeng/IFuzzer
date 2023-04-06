class A(object):
   def __repr__(self):
      return 'abc'

a = A()
a.__repr__ = lambda:'123'