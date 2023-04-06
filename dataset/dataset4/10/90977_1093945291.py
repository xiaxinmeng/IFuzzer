def _get_key(func: Callable) -> str:
    return f"{func.__module__}.{func.__qualname__}"

def overload(func):
    key = _get_key(func)
    _overloads.setdefault(key, []).append(func)
    return _overload_dummy

def get_overloads_for(func):
    key = _get_key(func)
    return _overloads.get(key, [])