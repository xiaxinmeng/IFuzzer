x = 1
def __gen(x):
  for i in range(10):
    yield x
g = __gen(x)