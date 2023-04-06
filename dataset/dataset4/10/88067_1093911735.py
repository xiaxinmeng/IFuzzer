@property
def __annotations__(self):
    if "__annotations__" not in self.__dict__:
        self.__dict__["__annotations__"] = {}
    return self.__dict__["__annotations__"]