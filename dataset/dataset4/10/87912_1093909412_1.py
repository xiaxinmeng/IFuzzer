
from ... import losses

class A:
  # AttributeError: 'Losses' object has no attribute 'Losses'
  losses: losses.Losses = losses.Losses()
