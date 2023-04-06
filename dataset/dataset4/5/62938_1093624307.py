def __format__(self, fmt):
  if len(fmt) >= 1 and fmt[-1] in 'oOxXdD':
    # treat like an int
    return format(self.value, fmt)
  else:
    # treat like a string
    format(str(self), fmt)