class something_else(object):
 pass

class foo(object):
 def __del__(self):
  self.__class__ = something_else

for _ in range(1000):
 foo()