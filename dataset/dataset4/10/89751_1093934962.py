import functools
import weakref

def weak_lru(maxsize=128, typed=False):
    'LRU Cache decorator that keeps a weak reference to "self"'

    proxy = weakref.proxy

    def decorator(func):

        _func = functools.lru_cache(maxsize, typed)(func)

        @functools.wraps(func)
        def wrapper(self, /, *args, **kwargs):
            return _func(proxy(self), *args, **kwargs)

        return wrapper

    return decorator