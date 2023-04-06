class Sentinel(type):
    @classmethod
    def __prepare__(cls, name, bases, **kwds):
        d = super().__prepare__(name, bases, **kwds)
        def __new__(cls_, *args, **kwargs):
            raise TypeError(
                f'{cls_!r} is a sentinel and cannot be instantiated')
        d.update(__new__=__new__)
        return d

    def __repr__(cls):
        return f'{cls.__module__}.{cls.__qualname__}'


class MISSING(metaclass=Sentinel): pass