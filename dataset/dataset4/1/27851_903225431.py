class I(int):
    def __floordiv__(self, other):
        return I(int(self) // other)