
import sys

def f():
  raise TypeError(42)

try:
  f()
except Exception as e:
  exc = e
  print('1--', e.__traceback__, sys.exc_info()[2])
  try:
    raise e
  except:
    pass
  print('2--', e.__traceback__, sys.exc_info()[2])
  raise
