def __matmul__(self, other):
  return sum(self[x] * other[x] for x in self.keys() | other.keys())