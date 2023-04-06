time.sleep(10)

def RANGE(a):
  # GENERATOR: Creates one output eachtime it is called.
  i=0
  while i<a:
    yield i
    i=i+1
  return