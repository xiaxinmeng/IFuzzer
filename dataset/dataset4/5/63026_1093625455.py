n = len(b)
a = [None]*n
for i,j in enumerate(range(n-1, -1, -1)): # reversed(range(n))
  a[i] = b[j]