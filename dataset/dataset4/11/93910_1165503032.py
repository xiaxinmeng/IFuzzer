class Color(Enum):
    RED = "Red"
    BLUE = "Blue"
    GREEN = "Green"

class FastColor:
    RED = Color.RED
    BLUE = Color.BLUE
    GREEN = Color.GREEN
    
def f():
    for _ in range(1000):
        Color.RED
        Color.BLUE
        Color.GREEN
        
import timeit
print(timeit.timeit('f()', number=10000, globals=globals()))

Color = FastColor
print(timeit.timeit('f()', number=10000, globals=globals()))