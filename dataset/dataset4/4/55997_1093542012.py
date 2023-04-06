class deco(object):
  def __init__(self, optional = False):
    self._optional = optional

  def __call__(self, decorated):
    decorated.optional = self._optional
    return decorated

@deco
class y(object):
  pass