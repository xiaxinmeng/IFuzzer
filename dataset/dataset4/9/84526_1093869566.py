import random

class MyRandom(random.Random):
    def getrandbits(self, n):
        return 0

my = MyRandom()
print([my.randint(1, 6) for _ in range(3)])
print([my.random() for _ in range(3)])