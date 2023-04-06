class WeakKeyDictionary(_collections_abc.MutableMapping):
    def __init__(self, dict=None):
        def remove(k, selfref=ref(self)):
            ...
        self._remove = remove
        ...

    def __setitem__(self, key, value):
        self.data[ref(key, self._remove)] = value