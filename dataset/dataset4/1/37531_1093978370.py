def sequpdate(self, iterable, value=True):
    for k in iterable:
        self[k] = value
    return self