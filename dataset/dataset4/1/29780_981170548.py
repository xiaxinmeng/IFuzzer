
import sys
import traceback

class Calc:
  def __init__(self):
     self.value = None
     self.exc_info = None

  def calc(self):
     raise TypeError(12)

  def calc_and_cache(self):
    try:
      self.value = self.calc()
      return self.value
    except Exception as e:
      self.exc_info = sys.exc_info()
      raise

  def get_cached_value(self):
    if self.exc_info is not None:
      raise self.exc_info[1]
    return self.value

c = Calc()

print('------ 1 ------')
try:
   c.calc_and_cache()
except Exception as e:
   traceback.print_exception(e)

print('------ 2 ------')
try:
   c.get_cached_value()
except Exception as e:
   traceback.print_exception(e)
