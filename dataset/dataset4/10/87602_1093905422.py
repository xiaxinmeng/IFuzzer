def test():
    from functools import lru_cache
    class No1:
        __eq__ = 0 .__eq__
        __hash__ = 0 .__hash__
    class No2:
        __eq__ = (0,).__contains__
        def __hash__(self, /): return hash(0)
    @lru_cache(256, typed=False)
    def test(v): return [v]
    test(No1()), test(No1()), test(0.0), test(0)
    
    print(test.cache_info())
    @lru_cache(256, typed=False)
    def test(v): return [v]
    test(No2()), test(No2()), test(0.0), test(0)
    print(test.cache_info())


    CacheInfo(hits=0, misses=4, maxsize=256, currsize=4)
CacheInfo(hits=2, misses=2, maxsize=256, currsize=2)