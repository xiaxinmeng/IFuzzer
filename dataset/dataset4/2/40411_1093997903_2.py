class C:                      # Emulated list type
  def __init__(self, d):
    self.data = d
  def __len__(self):
    return len(self.data)
  def __getitem__(self, item):
    if isinstance(item, slice):
      indices = item.indices(len(self))
      return [self[i] for i in range(*indices)]
    else:
      return self.data[item]

x = [1, 2, 3]
y = C([1, 2, 3])