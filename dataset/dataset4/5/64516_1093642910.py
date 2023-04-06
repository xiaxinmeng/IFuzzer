@contextmanager
def f():
 try:
  yield 6
 finally:
  throdbog() # woops, forgot to define this