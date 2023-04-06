import pyperf
from pyperf import Runner


def bench(loops):
    x = {1: "foo", 2: "baz"}
    t1 = pyperf.perf_counter()
    for _ in range(loops):
        try:
            x["fooz"]
        except KeyError:
            pass
    t2 = pyperf.perf_counter()
    return t2 - t1


runner = Runner()
runner.bench_time_func('bench exception handling', bench)