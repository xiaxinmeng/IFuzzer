import gc, sys
for i in range(100):
    class A:
        pass
    del A
    c = gc.collect()
    del c
    print(sys.gettotalrefcount())