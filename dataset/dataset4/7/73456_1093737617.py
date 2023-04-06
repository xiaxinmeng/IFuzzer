class Something(ctypes.c_ulong):
  def __repr__(self):
    return super(Something, self).value