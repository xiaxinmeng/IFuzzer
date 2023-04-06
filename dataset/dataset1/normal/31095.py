from functools import lru_cache
import gc

class Evil:
    def __del__(self):
        gc.collect()

def main():
    @lru_cache()
    def f(a):
        return Evil()
    f(1)

for i in range(100):
    print(i)
    main()
