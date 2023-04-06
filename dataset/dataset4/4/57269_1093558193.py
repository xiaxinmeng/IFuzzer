def RoundHalfUp(number):
  '''http://en.wikipedia.org/wiki/Rounding#Round_half_up
  0.5 and above round up else round down.
  '''
  trunc = int(number)
  fractionalPart = number - trunc
  if fractionalPart < 0.5:
    return trunc
  else:
    ceil = trunc + 1
    return ceil