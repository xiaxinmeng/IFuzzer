import _strptime
_strptime._cache_lock.acquire()
_strptime._TimeRE_cache = _strptime.TimeRE()
_strptime._regex_cache = {}
_strptime._cache_lock.release()