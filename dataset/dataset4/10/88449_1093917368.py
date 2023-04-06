class HashableDict(dict):
    def __new__(cls, pairs):
        return dict.__new__(cls, pairs)
    def __eq__(self, other):
        return tuple(self.mapping.items()) == tuple(other.sequence.items())
    def __hash__(self):
        return CONSTANT ^ hash(tuple(self.items()))
    def __getnewargs__(self):
        return tuple(self.items())
    
    # forbid all mutating methods
    __setitem__ = __delitem__ = update = __ior__ = None # etc.