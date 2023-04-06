
import random
import pickle

class MyRandom(random.Random):
    def __init__(self):
        super().__init__()
        self.getrandbits_calls = []
        print("init", self)

    def getrandbits(self, n):
        self.getrandbits_calls.append(n)
        return 0

rng = MyRandom()
print(rng.randbytes != random.Random.randbytes)
print()
rng2 = pickle.loads(pickle.dumps(rng))
print(rng2.randbytes != random.Random.randbytes)
