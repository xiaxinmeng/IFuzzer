def g(x, y):
  for i in x:
    for j in y:
      yield i, j

r2 = (0, 1)
[e for e in g(r2, g(r2, r2))]