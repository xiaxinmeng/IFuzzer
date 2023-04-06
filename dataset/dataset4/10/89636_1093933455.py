@classmethod
def from_name(cls, name):
    return cls[name]

@classmethod
def from_value(cls, value):
    return cls(value)