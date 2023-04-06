def compose(*args):
  def _composed(x):
    for f in args:
      x = f(x)
    return x
  return _composed