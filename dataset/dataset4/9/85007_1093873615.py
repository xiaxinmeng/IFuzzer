d1 = {'a': 1}
d2 = {'c': 3}
def fun(a, b, c):
    return a, b, c
print(fun(**d1, b='b', **d2))