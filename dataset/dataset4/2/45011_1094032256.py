class C:
   @classmethod
   def cm(cls): return cls.__name__
class D(C): pass
print(D.cm(), D().cm())