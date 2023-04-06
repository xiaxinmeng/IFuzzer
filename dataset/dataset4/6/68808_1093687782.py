import random
random.setstate((3, (1,)*624+(-10**9,), None))
random.random()