class B:
     def __bool__(self):
         raise AttributeError("don't do that!")

b = B()
try:
   if b:
        pass
except AttributeError:
   print("HI")