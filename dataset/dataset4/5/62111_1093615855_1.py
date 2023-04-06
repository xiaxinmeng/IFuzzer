def recurse(count, lookup_lines=True):
  if count> 0:
    return recurse(count - 1, lookup_lines=lookup_lines)
  if lookup_lines:
      return traceback.Stack.extract(traceback.walk_stack(None), lookup_lines=True)
  else:
      return traceback.Stack.extract(traceback.walk_stack(None), lookup_lines=False)

def doit():
    len(recurse(500))

def doit_lazy():
    len(recurse(500, False))