from collections import deque
_toss = deque()

def _compile(fmt):
    # Internal: compile struct pattern
    if len(_cache) >= _MAXCACHE:
        del _cache[_toss.popleft()]
    s = Struct(fmt)
    _cache[fmt] = s
    _toss.append(fmt)
    return s