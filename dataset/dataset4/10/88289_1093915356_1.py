class Sentinel:
    _instance = None
    _lock = Lock()
    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance
    def __repr__(self):
        *path_parts, classname = self.__class__.__qualname__.split('.')
        return '.'.join([self.__class__.__module__, *path_parts, classname.removeprefix('_')])


class _MISSING(Sentinel):
    pass
MISSING = _MISSING()