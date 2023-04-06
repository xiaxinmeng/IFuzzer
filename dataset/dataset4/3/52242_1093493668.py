def __format__(self, specifier):
  if len(specifier) == 0:
    return str(self)
  raise TypeError('non-empty format string passed to object.__format__')