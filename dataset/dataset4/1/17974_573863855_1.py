normal_cache = functools.lru_cache(typed=False)(func)
literal_cached = functools.lru_cache(typed=True)(func)

_cleanups.append(normal_cache.cache_clear)
_cleanups.append(literal_cached.cache_clear)