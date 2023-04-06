
class A:
    B = range(10)
    C = frozenset([4, 5, 6])
    D = list(i for i in B)
    E = list(i for i in B if i in C)
