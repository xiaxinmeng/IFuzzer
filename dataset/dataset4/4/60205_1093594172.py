def run_benchmark(bench):
    bench.timeit('S(123)', setup='S=str')
    bench.timeit('S(1) == S(2)', setup='S=str')
    bench.timeit('S(12345)', setup='S=str')
    bench.timeit('{S(x): x for x in data}', setup='data=tuple(range(100)); S=str')
    bench.timeit('"x=%s" % x', setup='x=123')
    bench.timeit('"x=%s" % x', setup='x=12345')