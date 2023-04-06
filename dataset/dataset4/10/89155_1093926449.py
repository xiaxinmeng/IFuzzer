def cache(func):
  _cache = {}
  @functools.wraps(func)
  def wrapped(*args, **kwargs):
    cache_key = tuple(args) + tuple(kwargs.items())
    if cache_key not in _cache:
      _cache[cache_key] = func(*args, **kwargs)
    return _cache[cache_key]
  return wrapped