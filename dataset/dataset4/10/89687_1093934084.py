                                                                                                  
from __future__ import annotations

import typing
from dataclasses import dataclass


def make_A():
  import collections

  @dataclass
  class A:
    x: collections.defaultdict

  return A


A = make_A()

@dataclass
class B(A):
  y: int

# NameError: name 'collections' is not defined
print(typing.get_type_hints(B.__init__))
