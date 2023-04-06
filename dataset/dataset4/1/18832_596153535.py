class B:
    def __add__(self, other):
        if not isinstance(other, B):
            return NotImplemented
        # return an instance of B representing self+other