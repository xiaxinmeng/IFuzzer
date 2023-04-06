# BEGIN OF FILE
class String(str):
    __slots__ = ()

name = String("hello")

class Bag:
    pass

o = Bag()
setattr(o, name, 42)