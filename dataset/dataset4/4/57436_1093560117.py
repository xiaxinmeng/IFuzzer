@lru_cache(typed=True)
def square(x):
    print('squaring', x)
    return x * x

for x in [3, 3.0, 3, 3.0]:
    print(square(x))