class b(object):
    __slots__ = ['_b__x']
    def __init__(self, x):
        self.__x = x
    
n = b(1)
n._b__x