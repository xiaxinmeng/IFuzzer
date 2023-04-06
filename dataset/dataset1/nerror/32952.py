"""
This file contains an illustation of the current and desired behaviour of
Mocks from unittest.mock Python module

A copy of this file is hosted on GitHub Gist: https://gist.github.com/s-kostyuk/81b5f0c92464af3b6a709b934debfcfe
"""
from unittest.mock import Mock

class SomeClass(object):
  def some_method(self):
    print("Hi!")

    
if __name__ == "__main__":
  ins = SomeClass()
  
  assert ins.some_method.__qualname__ == "SomeClass.some_method"
  
  mocked_ins = Mock(spec_set=SomeClass)
  
  print(mocked_ins.some_method.__qualname__)
  # Desired execution result: SomeClass.some_method
  # Current execution result: AttributeError: __qualname__
