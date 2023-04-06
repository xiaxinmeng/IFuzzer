foo = lru_cache()(partial(print, 'out'))
copy.deepcopy(foo)