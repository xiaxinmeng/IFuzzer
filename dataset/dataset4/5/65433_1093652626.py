from operator import ne
from itertools import repeat
class MyContainer:
  """container allowing equality search with containsEqual,
  while allowing fast identity search with __contains__:
  use "obj in c" to test if obj exactly sits in c
  use "c.containsEqual(obj)" to test if an object in c has c==obj
  """
  def containsEqual(self, object):
    return not all(map(ne, zip(repeat(object), self)))

  def __ne__(self, object):
    "Your not-equal test"