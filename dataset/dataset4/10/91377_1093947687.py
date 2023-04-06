import timeit

REPEATS = 100


def test1():
    selected = []
    for i in range(REPEATS):
        if i >= 25 and i <= 75:
            selected.append(i)
    return selected


def test2():
    selected = []
    for i in range(REPEATS):
        if 25 <= i <= 75:
            selected.append(i)
    return selected


print(timeit.timeit(test1))
print(timeit.timeit(test2))