def fullmatch(regex, input, flags=0):
  m = re.match(regex, input, flags)
  if m is not None and m.end() == len(input):
    return m
  return None