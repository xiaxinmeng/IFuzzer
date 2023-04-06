def is_local(self):
    return self.__scope in (LOCAL, CELL)