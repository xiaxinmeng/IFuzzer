def __getstate__(self):
    return [getattr(self, f.name) for f in fields(self)]


def __setstate__(self, state):
    for field, value in zip(fields(self), state):
        # use setattr because dataclass may be frozen
        object.__setattr__(self, field.name, value)