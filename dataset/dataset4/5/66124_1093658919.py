import _warnings

class Bla:
    def __del__(self, w=_warnings):
        w.warn_explicit('message', DeprecationWarning, 'x.py', 5)

bla = Bla()