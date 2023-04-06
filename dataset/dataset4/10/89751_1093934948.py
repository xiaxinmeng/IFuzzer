def cached_method(func):
    return cached_property(lambda self: lru_cache()(partial(func, self)))