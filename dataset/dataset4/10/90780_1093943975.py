def async_lru_cache(maxsize=128, typed=False):
    if callable(maxsize) and isinstance(typed, bool):
        user_function, maxsize = maxsize, 128
        return lru_cache(maxsize, typed)(reawaitable(user_function))

    def decorating_function(user_function):
        return lru_cache(maxsize, typed)(reawaitable(user_function))

    return decorating_function

def async_cached_property(user_function):
    return cached_property(reawaitable(user_function))