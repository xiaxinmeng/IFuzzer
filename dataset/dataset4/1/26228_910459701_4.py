_COROUTINE_TYPES = (types.CoroutineType, collections.abc.Coroutine)
_iscoroutine_typecache = set()


def iscoroutine(obj):
    """Return True if obj is a coroutine object."""
    if type(obj) in _iscoroutine_typecache:
        return True

    if isinstance(obj, _COROUTINE_TYPES):
        # Just in case we don't want to cache more than 100
        # positive types.  That shouldn't ever happen, unless
        # someone stressing the system on purpose.
        if len(_iscoroutine_typecache) < 100:
            _iscoroutine_typecache.add(type(obj))
        return True
    elif isinstance(obj, types.GeneratorType) and obj.gi_code.co_flags & inspect.CO_ITERABLE_COROUTINE:
        return True
    else:
        return False