from pyperf import Runner, perf_counter
from itertools import repeat

class A:
    pass

def bench(loops):
    a = A()
    a.x = 42
    it = repeat(None, loops)
    t0 = perf_counter()
    for x in it:
        a.x; a.x; a.x; a.x; a.x
        a.x; a.x; a.x; a.x; a.x
        a.x; a.x; a.x; a.x; a.x
        a.x; a.x; a.x; a.x; a.x
        a.x; a.x; a.x; a.x; a.x
    return perf_counter() - t0

runner = Runner()
runner.bench_time_func("a.x", bench, inner_loops=25)