class FakeFuture(futures.Future):

  def __init__(self, to_invoke):
    super(FakeFuture, self).__init__()
    self._to_invoke = to_invoke

  def result(self, timeout=None):
    return self._to_invoke()