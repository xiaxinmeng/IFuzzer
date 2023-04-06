def foo():
  ...
  tmp = bar(min, max)
  assert min <= tmp <= max
  return tmp