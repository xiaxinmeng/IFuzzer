class _AbcModulePlaceholder(type(_collections_abc)):
    def __warn(self):
        import warnings
        warnings.warn('collections.abc used without importing',
                      DeprecationWarning, 3)
    def __getattr__(self, name):
        self.__warn()
        return getattr(_collections_abc, name)
    def __setattr__(self, name, value):
        self.__warn()
        setattr(_collections_abc, name, value)
    def __delattr__(self, name):
        self.__warn()
        delattr(_collections_abc, name)
    def __dir__(self):
        self.__warn()
        return dir(_collections_abc)

abc = _AbcModulePlaceholder('abc')