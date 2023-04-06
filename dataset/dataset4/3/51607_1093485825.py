def save_object(r, key, m):
    r.set(key, cPickle.dumps(m))