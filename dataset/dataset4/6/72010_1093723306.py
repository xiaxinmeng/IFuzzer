class A:
    _dynamic_names = {}
    def __getattr__(self, name):
        if name in self._dynamic_names:
            return self._dynamic_names[name]
        raise AttributeError