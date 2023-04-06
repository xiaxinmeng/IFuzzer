class Blocked(object):
    def __getitem__(self): return 1
    def __len__(self): return 2
    __reversed__ = None