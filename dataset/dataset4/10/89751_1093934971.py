from functools import lru_cache

class CachedHash:
    @lru_cache
    def __hash__(self):
        # Expensive calculation because we are caching a big matrix for example.
        return 0

hashed = CachedHash()
hash(hashed) # => RecursionError: maximum recursion depth exceeded while calling a Python object