class attrmap:
    def __getitem__(self, key):
        return getattr(self, key)