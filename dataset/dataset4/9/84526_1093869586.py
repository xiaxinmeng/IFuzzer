from numpy.random import default_rng
import random

class NumpyRandom(random.BaseRandom):
    def __init__(self):
        self._rng = default_rng()

    def getrandbits(self, n):
        # FIXME: support n larger than 64 ;-)
        return int(self._rng.integers(2 ** n))

gen = NumpyRandom()
print(gen.randint(1, 6))
print(gen.random())
print(gen.randbytes(3))