def __newobj__(cls, *args):
     return cls.__new__(cls, *args)

class mydict(dict):
     def __reduce__(self):
         state = (dict(self), self.__dict__)
         return (__newobj__, (self.__class__,), state)