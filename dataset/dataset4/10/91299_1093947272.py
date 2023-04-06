import attr
import functools

@attr.s(slots=True)
class A:
    @staticmethod
    @functools.cache
    def incr(x):
        return x + 1

    @staticmethod
    @functools.lru_cache
    def incr_lru(x):
        return x + 1

obj = A()
print(obj.incr(1))
print(obj.incr_lru(2))