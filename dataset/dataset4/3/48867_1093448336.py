def f():
  e = 1
  del e
  def g(): print(e)
  return g