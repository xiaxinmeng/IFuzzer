class Foo:
    _getkey = attrgetter('x', 'y', 'z')
    def __key__(self): return self._getkey(self)