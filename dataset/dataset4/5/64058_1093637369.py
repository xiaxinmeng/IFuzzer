def spam(self, *args, **kwargs):
    @lru_cache(maxsize=20)
    def spam(foo, bar=1, *, baz=None):
        ...
    self.spam = spam
    return self.spam(*args, **kwargs)