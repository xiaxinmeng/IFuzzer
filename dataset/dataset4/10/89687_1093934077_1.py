
# b.py
from __future__ import annotations

import a
import typing

class B(a.A):
  pass

print(typing.get_type_hints(B))  
# {'x': <class 'collections.OrderedDict'>}
print(typing.get_type_hints(B.__init__))
# {'x': <class 'collections.OrderedDict'>, 'return': <class 'NoneType'>}
