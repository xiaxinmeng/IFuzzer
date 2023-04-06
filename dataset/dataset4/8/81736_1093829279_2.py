def __eq__(self, other):
    if isinstance(other, timedelta):
        return self._cmp(other) == 0
    else:
        return False