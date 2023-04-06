def isdisjoint(self, other):
    if self is other:
        if len(self) == 0:
            return True
        else:
            return False
    else:
        for item in other:
            if item in self:
                return False
        return True