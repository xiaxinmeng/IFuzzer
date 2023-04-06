import sys

class All(list):
    def public(self, api):
        sys.modules[api.__module__].__all__.append(api.__name__)

__all__ = All()

@__all__.public
def foo():
    pass

@__all__.public
class Bar:
    pass

__all__.append('CONST')
CONST = 1

print(__all__)