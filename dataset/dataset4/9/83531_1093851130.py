class myint(int):
    def __mul__(self, other):
        return type(self)(int(self)*int(other))
    @property
    def numerator(self):
        return type(self)(super().numerator)
    @property
    def denominator(self):
        return type(self)(super().denominator)