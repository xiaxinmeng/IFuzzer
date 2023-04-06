class BoundMod:
    def __init__(self, obj):
        self.obj = obj
    def __call__(self, otherarg):
        return self.obj % otherarg