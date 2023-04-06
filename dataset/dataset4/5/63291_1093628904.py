class Err:
  def __enter__(self): pass
  def __exit__(self, *exc): 1/0

class Ok:
  def __enter__(self): pass
  def __exit__(self, *exc): pass


import contextlib
s = contextlib.ExitStack()
s.push(Ok())
s.push(Err())
with s:
  pass