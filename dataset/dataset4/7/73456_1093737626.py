super_bypass_issue29270 = super

class Something(ctypes.c_ulong):
  def __repr__(self):
    return "BYPASS: " + super_bypass_issue29270(Something, self).__repr__()

s = Something(42)
print(s)