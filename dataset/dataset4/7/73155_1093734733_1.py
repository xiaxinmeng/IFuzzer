@functools.lru_cache(maxsize=2)
def f(v):
    time.sleep(.01)

threads = [threading.Thread(target=f, args=(v,)) for v in [1,2,2,3,2]]
for t in threads:
    t.start()