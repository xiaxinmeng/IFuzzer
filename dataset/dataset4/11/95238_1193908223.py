import pyperf
from pyperf import Runner


def bench(loops):
    x = object()
    t1 = pyperf.perf_counter()
    for i in range(loops):
        try:
            x.y
        except AttributeError:
            pass
    t2 = pyperf.perf_counter()
    return t2 - t1


runner = Runner()
runner.bench_time_func('bench exception handling', bench)