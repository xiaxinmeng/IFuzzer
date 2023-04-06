class Sentinel:
    def __new__(cls, *args, **kwargs):
        raise TypeError(f'{cls.__qualname__} cannot be instantiated')

class MISSING(Sentinel):
    pass