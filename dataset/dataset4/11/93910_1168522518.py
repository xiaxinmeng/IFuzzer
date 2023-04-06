from enum import Enum
import sys
import timeit

class Color(Enum):
    RED = "Red"
    BLUE = "Blue"
    GREEN = "Green"

class FastColor:
    RED = Color.RED
    BLUE = Color.BLUE
    GREEN = Color.GREEN
    
class OldStyleColor:
    RED = "Red"
    BLUE = "Blue"
    GREEN = "Green"
    
def f():
    for _ in range(1000):
        Color.RED
        Color.BLUE
        Color.GREEN
        
print(sys.version)
        
print(f"{timeit.timeit('f()', number=10000, globals=globals()):.2f}")

Color = FastColor
print(f"{timeit.timeit('f()', number=10000, globals=globals()):.2f}")

Color = OldStyleColor
print(f"{timeit.timeit('f()', number=10000, globals=globals()):.2f}")