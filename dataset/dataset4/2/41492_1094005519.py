class attrmap:
    def __init__(self, obj):
        self.obj = obj
    def __getitem__(self, key):
        return getattr(self.obj, key)