class NoneDict(dict):
    """
    Dictionary implementation that always returns None when a key is not in
the dict,
    rather than raising a KeyError
    """
    def __getitem__(self, key):
        try:
            val = dict.__getitem__(self, key)
        except KeyError:
            val = None
        return val