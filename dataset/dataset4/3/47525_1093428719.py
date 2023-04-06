import dis
def foo():
  if 0 and 1: return "hi"

dis.dis(foo)