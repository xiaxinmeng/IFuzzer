import math

class TrigConst: 
    const = math.pi
    def __get__(self, obj, objtype=None):
        print("__get__ called")
        return self.const
    
    def __set__(self, obj, value):
        print("__set__ called")
        self.const = value
        

class Trig:
    const = TrigConst()              # Descriptor instance