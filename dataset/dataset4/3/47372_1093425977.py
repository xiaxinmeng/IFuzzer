class C(object):
   def setx(self): self.__x = 42
   x = property(lambda self: self.__x)