from functools import cached_property, lru_cache

class A:
    @property
    def a(self): return ''

    @cached_property
    def b(self): return ''
    
    @property
    @lru_cache
    def c(self):
        return ""


print(isinstance(A.a, property))
print(isinstance(A.b, property))
print(isinstance(A.c, property))