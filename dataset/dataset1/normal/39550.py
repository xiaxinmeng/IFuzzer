class T(tuple):
    def __iter__(self):
            yield self

isinstance(3, T())
