def atcat(self, src,  src_at, dst):
  res = []
  for col in getattr(self, src):
    res += getattr(col, src_at)
  setattr(self, dst, res)