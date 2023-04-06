def ignore_extra_args(base):
    base_meta = type(base)
    class _FilteredMeta(base_meta):
        def __new__(*args, **kwds):
            return base_meta.__new__(*args)
        def __init__(*args, **kwds):
            return base_meta.__init__(*args)
    class _Filtered(base, metaclass=_FilteredMeta):
        pass
    return _Filtered

class InitX():
    def __init_subclass__(cls, x=None):
        print('x')

from abc import ABCMeta
class Abstract(metaclass=ABCMeta):
    pass

class AbstractWithInit(ignore_extra_args(Abstract), InitX, x=1):
    pass

AbstractWithInit()