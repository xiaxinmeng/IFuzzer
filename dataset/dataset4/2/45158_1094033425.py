_default = object()

def getitem(iterable, index, default=_default):
   try:
      return list(iterable)[index]
   except IndexError:
      if default is _default:
         raise
      return default