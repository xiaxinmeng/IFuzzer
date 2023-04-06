class Ordered(Iterable):
    def __eq__(self, other):
        if not isinstance(other, Ordered):
            return NotImplemented
        return all(i == j for (i, j) in zip(self, other))