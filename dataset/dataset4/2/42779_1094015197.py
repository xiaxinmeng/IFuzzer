pycon
"""
>>> class A(object):
...   def foo(self): pass
...
>>> id(A.foo) == id(A.foo)
True
>>> A.foo is A.foo
False
>>>
>>> a = A()
>>> id(a.foo) == id(a.foo)
True
>>> a.foo is a.foo
False
"""
