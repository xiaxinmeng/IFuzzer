def outer():
  x = 0
  y = (x for i in range(10))
  del x  # SyntaxError