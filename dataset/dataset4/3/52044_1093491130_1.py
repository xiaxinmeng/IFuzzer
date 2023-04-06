class NamedTuple(Sequence):
    @classmethod
    def __subclasshook__(cls, C):
        if cls is NamedTuple:
            if any("_fields" in B.__dict__ or  # for namedtuple
                   "n_fields" in B.__dict__  # for structseq
                   for B in C.__mro__):
                return True
        return NotImplemented