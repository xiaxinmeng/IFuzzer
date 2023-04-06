def IsNan(x):
  if isinstance(x, list) or isinstance(x, tuple) or isinstance(x, set):
    for i in x:
      if IsNan(i):
        return True
    return False
  else:
    return (x is x) and (x != x)