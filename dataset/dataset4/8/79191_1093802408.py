class reverted_order:
    def __init__(self, value):
        self.value = value
    def __lt__(self, other):
        if isinstance(other, reverted_order):
            other = other.value
        return self.value.__ge__(other)
    # __le__, __gt__, __ge__, __eq__, __ne__, __hash__