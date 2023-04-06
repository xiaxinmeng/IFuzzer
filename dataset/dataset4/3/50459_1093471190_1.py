@classmethod
def no_context(cls, *args, **kwds):
  exc = cls(*args, **kwds)
  exc.__context__ = ExceptionContextSuppressed
  return exc