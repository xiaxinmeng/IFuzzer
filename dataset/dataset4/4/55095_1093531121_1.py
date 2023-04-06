def MyQueue():
    import cPickle
    def myput(obj, *args, **kwargs):
        cPickle.dumps(obj)
        return orig_put(obj, *args, **kwargs)

    q = Queue()
    orig_put, q.put = q.put, myput
    return q