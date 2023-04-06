import random
seed = 199
choices = range(-10,12)

for k in range(10):
    random.seed(seed)
    print(random.sample(choices,k))