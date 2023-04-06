import perf
bench = perf.Runner()
bench.timeit("namedtuple.attr",
             "a.a",
             "from collections import namedtuple as n; a = n('n', 'a b c')(1, 2, 3)",
             duplicate=20)