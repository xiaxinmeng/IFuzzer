cache = weakref.WeakValueDictionary()

class Bar:
    pass

class Foo:
    def __init__(self):
        self._self = self
        self.value = Bar()
        cache[id(self.value)] = self.value

    def __del__(self):
        # the cache may or may not have self.value at this point
        # even though self.value is strongly referenced!
        print(list(cache.items()))