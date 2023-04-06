@contextlib.contextmanager
def managed_resource():
  resource = acquire()
  try:
    yield resource
  finally:
    resource.release()

class ManagedResource:
  def __init__(self):
    self.resource = acquire()
  def __enter__(self):
    return self.resource
  def __exit__(self, *args):
    self.resource.release()