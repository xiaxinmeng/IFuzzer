import timeit
print(min(timeit.repeat("(a,)", setup="a = 1; b = 1", repeat=5, number=10**7)))
print(min(timeit.repeat("(a, b)", setup="a = 1; b = 1", repeat=5, number=10**7)))