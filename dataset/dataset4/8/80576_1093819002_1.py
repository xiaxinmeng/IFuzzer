class FakeFuture(object):

  def __init__(self, to_invoke):
    self._to_invoke = to_invoke

  def result(self, timeout=None):
    return self._to_invoke()