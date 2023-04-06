cache = {}
def stat(path):
    if cache.has_key(path):
        return cache[path]