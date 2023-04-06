class C(object):
    def __iter__(self):
        yield 'yes!'
    def __radd__(self, other):
        other.append('bug!')
        return other
    def __rmul__(self, other):
        other *= 2
        return other
    def __index__(self):
          return 3

class L(list):
    def __iadd__(self, other):
        list.__iadd__(self,other)
        return self
    def __mul__(self, other):
        return L(list.__imul__(self,other))