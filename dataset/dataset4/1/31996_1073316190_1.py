dict[str, int](a=1, b=2)      # 359 ns +- 6 ns -> 280 ns +- 3 ns: 1.29x faster
list[int](())                 # 259 ns +- 3 ns -> 246 ns +- 5 ns: 1.05x faster
MappingProxyType[str, int](d) # 273 ns +- 13 ns -> 261 ns +- 4 ns: 1.05x faster

class A:
    def __init__(self, a, b):
        pass
G = GenericAlias(A, int)
G(1, 2)                       # 198 ns +- 6 ns -> 190 ns +- 4 ns: 1.04x faster