def __eq__(self, other):
    if isinstance(other, self.__class__):
        return self.value == other.value
    return False