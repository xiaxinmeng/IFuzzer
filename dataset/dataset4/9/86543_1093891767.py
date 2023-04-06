
from __future__ import annotations
from typing import TYPE_CHECKING, Optional, cast
if TYPE_CHECKING:
   class A:
     pass

def f(a: A):
   pass


f(cast(A, "anything"))
