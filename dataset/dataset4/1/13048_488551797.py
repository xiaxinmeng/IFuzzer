def lru_cache(*args, **kwargs):
    if not kwargs and len(args) == 1 and callable(args[0]):
        return lru_cache_impl()(args[0])
    return lru_cache_impl(*args, **kwargs)

lru_cache.__text_signature__ = '(maxsize=128, typed=False)'

def lru_cache_impl(maxsize=128, typed=False):
    ... # the current implementation