class ConstantMap:
    markdict = {}

    def __init__(self):
        """add new global symbols to instance's name map"""
        self.names = {}
        import types
        for key,val in globals().items():
            if (not self.markdict.has_key(key) and
                key[:2] != "__" and
                type(val) not in [types.InstanceType,
types.ClassType]):
                self.names[val] = key
        self.markdict.update(globals())

    def __call__(self, key):
        """return a name mapping"""
        return self.names[key]

    def mark(self):
        """checkpoint current globals"""