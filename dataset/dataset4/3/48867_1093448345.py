def outer():
  x = 0
  def inner(): return x
  del x  # SyntaxError