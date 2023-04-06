@classmethod
def register(cls, subclass):
    type(cls).register(cls, subclass)
    sys._register_tpflags_mapping(subclass)  # or sequence

@classmethod
def __subclasshook__(cls, subclass):
    if sys._check_tpflags_mapping(subclass):  # or sequence
        return True
    return NotImplemented