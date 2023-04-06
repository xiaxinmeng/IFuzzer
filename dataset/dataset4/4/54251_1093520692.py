class Foo:
    ...
    def __lt__(self, other):
        if not isinstance(other, Foo):
            return NotImplemented
        return self.some_value < other.some_value