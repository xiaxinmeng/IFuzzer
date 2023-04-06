def f(x): return x
def broken(): return 1
print(f(*(broken() for x in (0,))))
# prints 1