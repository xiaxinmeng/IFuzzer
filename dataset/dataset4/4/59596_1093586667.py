def bitl(x):
  x = abs(x)
  n = 0
  while x > 0:
    n = n+1
    x = x>>1
  return n