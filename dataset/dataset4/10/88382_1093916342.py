def do_something(self, a, b=None):
  b = b if b is not None else []
  b.append(a)
  print('b contains', b)