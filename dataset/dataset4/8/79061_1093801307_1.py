

len = 1
def g():
   from builtins import len

   return len([1, 2, 3])

g() # => 3

AssertionError = +1

def f():
   from builtins import AssertionError
   assert False

f() # boooom


