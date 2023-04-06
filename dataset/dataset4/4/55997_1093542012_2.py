def deco(_decorated = None, optional = False):
  def _wrapped(decorated):
    decorated.optional = optional
    return decorated
  if _decorated is not None:
    return _wrapped(decorated)
  return _wrapped