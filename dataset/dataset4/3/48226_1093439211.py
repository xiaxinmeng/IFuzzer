class safe_key(object):
    __slots__ = ('obj',)

    def __init__(self, obj):
        self.obj = obj

    def __eq__(self, other):
        return self.obj.__eq__(other.obj)

    def __lt__(self, other):
        try:
            return self.obj < other.obj
        except TypeError:
            return id(type(self.obj)) < id(type(other.obj))


ls = [2, 1, 1.0, 1.5, 'a', 'c', 'b']
print(sorted(ls, key=safe_key))