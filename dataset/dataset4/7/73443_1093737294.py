from abc import ABCMeta, abstractproperty

class C:
    __metaclass__ = ABCMeta
    def getx(self): pass
    def setx(self, value): pass
    x = abstractproperty(getx, setx)
 
class D(C):
    @property
    def x(self):self._x
 
d = D()    
print(d)   