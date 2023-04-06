import traceback

def recurse(count):
  if count> 0:
    return recurse(count - 1)
  return traceback.format_stack()

def doit():
    len(recurse(500))