
class Flag(Enum, boundary=STRICT):
    def __reduce_ex__(self, proto):
        return self.__class__, (self._value_, )
