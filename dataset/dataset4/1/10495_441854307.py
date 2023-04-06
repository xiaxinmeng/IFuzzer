import perf

runner = perf.Runner()
runner.timeit("collections.namedtuple('A','x')", 
stmt="collections.namedtuple('A','x')", 
setup="import collections")