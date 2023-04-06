from enum import *
class Foo(Flag):
    A = auto()      # 1
    B = auto()      # 2
    AB = A | B      # 3 (1 | 2)
    AC = auto() | A # Fails, but should be 5 (1 | 4)
    ABD = auto() | A | B # Just taking it one step further to make a point, 11 (1 | 2 | 8)