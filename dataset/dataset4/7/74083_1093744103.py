def __copy__(self):
    cls, *args = self.__reduce__()
    return cls(*map(copy, args))