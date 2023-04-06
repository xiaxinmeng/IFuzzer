class LazyFile:
   def __init__(self, name, mode="r"):
      self.name = name
      self.mode = mode
   def __iter__(self):
      return open(self.name, self.mode)
  
import operator
  
f = LazyFile("does not exist")
  
s = reduce(operator.add, f)