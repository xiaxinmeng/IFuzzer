
import random
import pickle

class MyRandom(random.Random):
    def __init__(self):
        super().__init__()

    def getrandbits(self, n):
        return 0

rng = MyRandom()
print(MyRandom.randbytes is random.Random._randbytes_getrandbits)
randbytes2 = pickle.loads(pickle.dumps(MyRandom.randbytes))
print(randbytes2 is random.Random._randbytes_getrandbits)
