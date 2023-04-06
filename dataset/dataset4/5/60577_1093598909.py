import collections.abc
class S(collections.abc.Set):
    def __contains__(self, key): return False
    def __iter__(self): return iter(())
    def __len__(self): return 0