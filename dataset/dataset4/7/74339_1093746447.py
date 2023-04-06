@functools.lru_cache()
def func(param):
  ...

func.invalidate(PARAM) # discard this cached call, or ignore if not cached