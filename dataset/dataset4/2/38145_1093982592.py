class FakeMod:
   def __init__(self, n):
      self.__name__ = n
   def foo(self):
      return 42

import sys