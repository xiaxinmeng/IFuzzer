def __isub__(self, it):
    if it is self:
        self.clear()
    else:
        for value in it:
            self.discard(value)
    return self