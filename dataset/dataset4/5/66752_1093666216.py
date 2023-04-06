cache = {}
if not fields in cache:
    cache[fields] = new_namedtuple
return cache[fields]