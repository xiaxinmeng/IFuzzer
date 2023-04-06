class JSParsingError(Exception):
    pass


class JS:
    def __init__(self, obj, path=None) -> None:
        self.__raw__ = obj

    def __getattr__(self, name):
        with self:
            if isinstance(self.__raw__, dict):
                return JS(self.__raw__[name], self.__path + [name])
            return JS(getattr(self.__raw__, name), self.__path + [name])

    def __setattr__(self, name, val):
        with self:
            if isinstance(self.__raw__, dict):
                self.__raw__[name] = val
            setattr(self.__raw__, name, val)

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        if exception_value is None:
            return False
        if isinstance(exception_value, Exception):
            raise JSParsingError(self.__path) from exception_value
        return False

JS({})
