class safe_key(object):

    __slots__ = ('obj',)

    def __init__(self, obj):
        self.obj = obj

    def __eq__(self, other):
        return self.obj.__eq__(other.obj)

    def __lt__(self, other):
        rv = self.obj.__lt__(other.obj)
        if rv is NotImplemented:
            rv = id(type(self.obj)) < id(type(other.obj))
        return rv


ls = [2, 1, 1.0, 1.5, 'a', 'c', 'b']
print(sorted(ls, key=safe_key))