class Repeater: # this class is similar to itertools.repeat
   def __init__(self, o, t):
       self.o = o
       self.t = int(t)
   def __iter__(self): # its iterator is itself
       return self
   def __next__(self):
       if self.t > 0:
           self.t -= 1
           return self.o
       else:
           raise StopIteration