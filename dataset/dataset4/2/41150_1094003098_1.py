class Mutable:
  def __init__(self): self.bracketed=[self]
  # Create list, REDUCE, then populate list
  def __reduce__(self): return id,(self.bracketed,)