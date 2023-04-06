from abc import ABCMeta
class Initifier:
    def __init_subclass__(cls, x=None, **kwargs):
        super().__init_subclass__(**kwargs)
        print('got x', x)

class Abstracted(metaclass=ABCMeta):
    pass

class Thingy(Abstracted, Initifier, x=1):
    pass

thingy = Thingy()