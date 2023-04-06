
class A:
  # Type correctly inferred and no closure runtime error
  losses: 'losses.Losses' = losses.Losses()
