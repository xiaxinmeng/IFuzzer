class FakeExecutor(futures.Executor):

  def submit(self, f, *args, **kwargs):
    future = futures.Future()
    future.set_result(f(*args, **kwargs))
    return future

  def shutdown(self, wait=True):
    pass