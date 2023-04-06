class TwoWayDictionary(dict):
    __slots__ = ()
    def __setitem__(self, key, value):
        dict.__setitem__(self, key, value)
        dict.__setitem__(self, value, key)