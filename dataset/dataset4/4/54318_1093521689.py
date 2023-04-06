def gen():
  l = [itertools.permutations(range(10)) for _ in range(10)]
  g = itertools.product(*l)
  for i in g:
    yield i