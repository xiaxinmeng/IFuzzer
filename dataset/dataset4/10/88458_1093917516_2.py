import contextlib

@contextlib.contextmanager
def cm():
  print("acquire cm")
  try:
    yield 1
  finally:
    print("release cm")

class CM:
  def __init__(self):
    print("acquire CM")
  def __enter__(self):
    return 1
  def __exit__(self, *args):
    print("release CM")

def f1():
  with contextlib.ExitStack() as es:
    es.enter_context(cm())
    es.pop_all()

def f2():
  with contextlib.ExitStack() as es:
    es.enter_context(CM())
    es.pop_all()

f1()
f2()