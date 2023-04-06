def merge_dicts(*args):
  result = {}
  for x in args:
    result.update(x)
  return result