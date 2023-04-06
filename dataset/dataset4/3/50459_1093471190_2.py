@classmethod
def no_context(cls, *args, **kwds):
  exc = cls(*args, **kwds)
  exc.__context__ = None
  exc._add_context = False
  return exc