class Test:
   def __iter__(self):
      raise IOError

reduce(lambda x,y: x+y, Test())