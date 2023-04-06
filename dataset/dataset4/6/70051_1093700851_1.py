def __reversed__(self):
    keys = [k for k in self.keys()]
    return (self[k] for k in reversed(keys))