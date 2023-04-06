import gc
TAG = object()

def monitor():
    lst = [x for x in gc.get_referrers(TAG)
           if isinstance(x, tuple)]
    t = lst[0]   # this *is* the result tuple
    print(t)     # full of nulls !
    return t     # Keep it alive for some time

def my_iter():
    yield TAG    # 'tag' gets stored in the result tuple
    t = monitor()
    for x in range(10):
        yield x  # SystemError when the tuple needs to be resized

tuple(my_iter())