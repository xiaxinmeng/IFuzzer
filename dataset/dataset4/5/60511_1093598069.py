def map_async(self, func, iterable, chunksize=None, callback=None,
        error_callback=None):
    '''
    Asynchronous version of `map()` method.
    '''
    return self._map_async(func, iterable, mapstar, chunksize)