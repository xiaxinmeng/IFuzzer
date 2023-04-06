from dataclasses import *

class B:
   def __init__(self, a, b, c):
       # do something with a, b, c, and maybe use fields(self) to figure out we
       # have a "i" field
       self.i = a + b + c

@dataclass
class C(B):
   i: int

   def __init__(self, a, b, c):
       super().__init__(a, b, c)

c = C(1, 2, 3)