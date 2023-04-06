def __eq__(self, other):
    if isinstance(other, OrderedDict):
        if not dict.__eq__(self, other):
            return False
        return all(p == q for p, q in _zip_longest(self.items(),
                                                   other.items()))
    return dict.__eq__(self, other)