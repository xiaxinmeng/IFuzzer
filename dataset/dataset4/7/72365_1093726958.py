@lru_cache
def foo(i):
  return i*2
foo(1)    # -> add 1 as key in the cache
foo(2)    # -> add 2 as key in the cache
foo.clear_cache() # -> this clears the whole cache
foo.clear_cache(1) # -> this would clear the cache entry for 1