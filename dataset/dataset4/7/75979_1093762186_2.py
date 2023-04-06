class UnsettableFile:
    def __getattr__(self, name):
        return __file__
    def __setattr__(self, name, value):
        raise TypeError()