class SomethingView():
    @functools.lru_cache()
    def get_object(self):
        return self._object