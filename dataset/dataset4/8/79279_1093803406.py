class Color(object):
    __slots__ = (('name',))

    def __init__(self, name):
        self.name = name

green = Color('green')  #   Works
assert green.name == 'green'

Color.__new__ = 0
del Color.__new__

red = Color('red')      #   Fails in Python 3; works in Python 2 & pypy
assert red.name == 'red'